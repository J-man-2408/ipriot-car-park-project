from display import Display
from sensors import Sensor, TemperatureSensor
import json
from pathlib import Path
from datetime import datetime


class CarPark:
    """
    Represents a car park with sensors, displays, and vehicle tracking.
    """
    
    def __init__ (self, location="Unknown", capacity=0, plates=None, displays=None, sensors=None, log_file=Path("log.txt")):
        """
        Initializes a new CarPark object.
        
        Args:
            location (str): Name or address of the car park. Default is "Unknown".
            capacity (int): Total number of parking bays. Default is 0.
            plates (list of str, optional): List to store license plates. Default is empty list.
            displays (list of Display, optional): List of Display objects. Default is empty list.
        """
        self.location = location
        self._display = displays or []
        self.capacity = capacity
        self._plate = plates or []
        self.sensors=sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.current_temperature = 20
        
        
    def __str__ (self):
        """
        Returns a readable string representation of the CarPark object.
        """
        return f"The carpark at {self.location} has {self.capacity} bays"
    
    def register(self, component):    
        """
        Register a sensor or display with the car park.
        """    
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
            component.car_park = self 
            
        elif isinstance(component, Display):
            self._display.append(component)
            
    @property
    def plates(self):
        """
        Returns list of current plates in the car park
        """
        return self._plate

    @property
    def displays(self):
        """
        Return list of displays in the car park.
        """
        return self._display

       
    @property    
    def available_bays(self):
        """
        Returns the number of available bays in the car park. 
        This is a derived value of the capacity minus number of parked cars
        Never returns a negative number
        """
        return max(0, self.capacity - len(self._plate))
    
    def add_car(self, plate):
        """
        Add a car to the car park and update displays.
        """
        print (f"Welcome to {self.location}")
        if plate in self.plates:
            print("Car is already parked.")
            return

        if len(self.plates) >= self.capacity: # Checks BEFORE adding
            print("Car park is FULL!")
            return
        
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")
            
    def remove_car(self, plate):
        """
        Remove a car from the car park and update display s
        """
        print (f"{self.location} will see you next time!")
        if plate not in self.plates:
            raise ValueError(f"Car {plate} was not found")

        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")
    
    def update_displays(self):
        """
        Update all displays with current available bays and temperature
        """
        for sensor in self.sensors:
            if isinstance(sensor, TemperatureSensor):
                sensor.update_car_park()

        data = {
            "available_bays": self.available_bays,
            "temperature": self.current_temperature
        }

        for display in self._display:
            display.update(data)
    
    def _log_car_activity(self, plate, action):
        """
        Log car entry/exit activity to the log file.
        """
        with self.log_file.open("a") as f:
         f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
         
    
    #json configuration
    def write_config(self):
        """
        Write car park configuration to JSON file.
        """
        with Path("config.json").open("w") as f:
            json.dump({
                "location": self.location,
                "capacity": self.capacity,
                "log_file": str(self.log_file)
            }, f)
    
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """
        Create car park instance from JSON configuration.
        """
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
           config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

                    
