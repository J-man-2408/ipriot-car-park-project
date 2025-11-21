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
            
    @property    
    def available_bays(self):
        """
        Returns the number of available bays in the car park. 
        This is a derived value of the capacity minus number of parked cars
        Never returns a negative number
        """

        return max(0, self.capacity - len(self._plate))
    
    def add_car(self, plate):
        if plate in self._plate:
            print ("Car is already parked.")
            return
        
        if len (self._plate) >= self.capacity:
            print ("Car park is FULL!")
            return
        
        self._plate.append(plate)
        self.update_displays()
        print (f"Car {plate} added. {self.available_bays} bays remaining.")
            
    def remove_car (self, plate):
        if plate not in self._plate:
            print ("Car was not found")
            return
        
        self._plate.remove(plate)
        self.update_displays()
        print(f"Car {plate} removed. {self.available_bays} bays remaining.")
    
    def update_displays (self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 20 #CHANGE FOR SENSOR READING EVENTUALLY !!!
        }
        for display in self._display:
            display.update(data)
                    
# testing inputs

from sensors import EntrySensor, ExitSensor
from display import Display
from car_park import CarPark

location = "Kalamunda"
capacity = 5
carpark = CarPark(location, capacity)


entry = EntrySensor(id=1)
exit_ = ExitSensor(id=2)


d1 = Display(id=101)
d2 = Display(id=102)


carpark.register(entry)
carpark.register(exit_)
carpark.register(d1)
carpark.register(d2)


print("Checking sensors' car park references:")
print(entry.car_park)  # Should show CarPark object
print(exit_.car_park)  # Should show CarPark object
print()

print("Initial display states:")
carpark.update_displays()
print()

print("Simulating vehicle entries:")
for _ in range(3):
    entry.detect_vehicle()
print()


print("Simulating vehicle exits:")
for _ in range(2):
    exit_.detect_vehicle()
print()

print("Final car park plates list:", carpark._plate)
print("Final available bays:", carpark.available_bays)
print("Final display states:")
carpark.update_displays()

