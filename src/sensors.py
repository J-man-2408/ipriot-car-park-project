import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__ (self, id, is_active=False, car_park=None):
        self.id=id
        self.is_active=is_active
        self.car_park=car_park
    
    def __str__ (self):
        status = "active" if self.is_active else "inactive"
        return f"Sensor {self.id} ({status})"
    
    @abstractmethod
    def update_car_park(self, plate):
        pass
    
    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0, 999), "03d")
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)
        
class EntrySensor(Sensor):
    def update_car_park(self, plate):
        """Add the car to the car park"""
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def _scan_plate(self):
        if self.car_park and self.car_park._plate:
            return random.choice(self.car_park._plate)
        return None

    def update_car_park(self, plate):
        if plate:
            self.car_park.remove_car(plate)
            print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
