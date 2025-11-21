import unittest
from sensors import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("234 This Street", 10)
        self.entry_sensor = EntrySensor(id=1)
        self.exit_sensor = ExitSensor(id=2)
        self.car_park.register(self.entry_sensor)
        self.car_park.register(self.exit_sensor)

    def test_entry_sensor_detect_vehicle_adds_car(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)

    def test_exit_sensor_detect_vehicle_removes_car(self):
        self.car_park.add_car("FAKE-001")
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 0)

if __name__ == "__main__":
    unittest.main()
