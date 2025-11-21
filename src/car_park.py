from display import Display
from sensors import Sensor

class CarPark:
    def __init__ (self, location="Unknown", capacity=0, plates=None, displays=None, sensors=None):
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
        
    def __str__ (self):
        """
        Returns a readable string representation of the CarPark object.
        """
        return f"The carpark at {self.location} has {self.capacity} bays"
    
    def register(self, component):        
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
            component.car_park = self 
            
        elif isinstance(component, Display):
            self._display.append(component)
    
    def add_car(self, plate):
        if plate not in self._plate:
            if len (self._plate) < self.capacity:
                self._plate.append(plate)
                self.update_displays()
            else: 
                print("Car park is FULL!")
        else: 
            print("Car is already parked.")
            
    def remove_car (self, plate):
        if plate in self._plate:
            self._plate.remove(plate)
            self.update_displays()
        else:
            print ("Car was not found.")
    
    def update_displays (self):
        for display in self._display:
            display.update()
                    
# testing inputs
if __name__ == "__main__":
    from sensors import EntrySensor, ExitSensor
    from display import Display

    # Create car park
    location = "Kalamunda"
    capacity = 15
    carpark = CarPark(location, capacity)

    # Create sensors
    entry = EntrySensor(id=1)
    exit_ = ExitSensor(id=2)

    # Create displays
    d1 = Display(id=101, message="Welcome!")
    d2 = Display(id=102, message="Have a nice day!")

    # Register sensors and displays
    carpark.register(entry)
    carpark.register(exit_)
    carpark.register(d1)
    carpark.register(d2)

    # Check if sensors have bidirectional link
    print(entry.car_park)   # Should print the CarPark object
    print(exit_.car_park)   # Should print the CarPark object

    # Check displays list
    for d in carpark._display:
        print(d)  # Should print display info

    # Test add_car / remove_car
    carpark.add_car("ABC123")
    carpark.add_car("XYZ789")
    print(carpark._plate)  # Should show the two plates

    carpark.remove_car("ABC123")
    print(carpark._plate)  # Should show only "XYZ789"
