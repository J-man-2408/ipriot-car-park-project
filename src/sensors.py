import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    Base abstract class for car park sensors.
    """
    def __init__ (self, id, is_active=False, car_park=None):
        """
        Initializes Sensor object.
        
        Args:
            id: id of the sensor.
            is active (bool): Sets the sensors activity to false by default
            car_park: Sets the car_park that the sensor is assigned to as None by default
        """
        self.id=id
        self.is_active=is_active
        self.car_park=car_park
    
    def __str__ (self):
        """
        Return readable string of sensor
        """
        status = "active" if self.is_active else "inactive"
        return f"Sensor {self.id} ({status})"
    
    @abstractmethod
    def update_car_park(self, plate):
        pass
    
    def _scan_plate(self):
        """
        Generates a fake license plate number.
        """
        return "FAKE-" + format(random.randint(0, 999), "03d")
    
    def detect_vehicle(self):
        """
        Detect a vehicle and trigger update on car park.
        """
        plate = self._scan_plate()
        self.update_car_park(plate)
        
class EntrySensor(Sensor):
    """
    Sensor to detect incoming vehicles.
    """
    def __init__(self, id, is_active=False, car_park=None, display=None):
        super().__init__(id, is_active, car_park)
        self.display = display

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")
        for sensor in self.car_park.sensors:
            if isinstance(sensor, TemperatureSensor):
                sensor.update_car_park()
        if self.display:
            self.display.update({"available_bays": self.car_park.available_bays,
                                 "temperature": self.car_park.current_temperature})
            print()


class ExitSensor(Sensor):
    """
    Sensor to detect exiting vehicles.
    """
    def __init__(self, id, is_active=False, car_park=None, display=None):
        super().__init__(id, is_active, car_park)
        self.display = display

    def _scan_plate(self):
        if self.car_park and self.car_park._plate:
            return random.choice(self.car_park._plate)
        return None  

    def update_car_park(self, plate):
        if plate:
            self.car_park.remove_car(plate)
            print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
            for sensor in self.car_park.sensors:
                if isinstance(sensor, TemperatureSensor):
                    sensor.update_car_park()
            if self.display:
                self.display.update({
                    "available_bays": self.car_park.available_bays,
                    "temperature": self.car_park.current_temperature
                })
                print()
        else:
            print("No cars to remove")

            
class TemperatureSensor(Sensor):
    """
    Sensor to simulate car park temperature.
    """
    def update_car_park(self):
        if self.car_park:
            # simulate temperature reading
            temp = round(random.uniform(18, 28), 1)
            self.car_park.current_temperature = temp

