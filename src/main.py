# Author: Jasmine (J-man-2408)
# 20147280

from car_park import CarPark
from sensors import EntrySensor, ExitSensor, TemperatureSensor
from display import Display

def main():
    """
    Main function to create the car park, sensors, and simulate vehicles entering and exiting.
    """
    
    # Create car park and write config
    car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")
    car_park.write_config()  # writes moondalup_config.json
    car_park = CarPark.from_config("config.json")
    
    # Create displays
    entry_display = Display(id=1, is_on=True)
    exit_display = Display(id=2, is_on=True)

    # Create sensors with associated displays
    entry_sensor = EntrySensor(id=1, is_active=True, display=entry_display)
    exit_sensor = ExitSensor(id=2, is_active=True, display=exit_display)
    temp_sensor = TemperatureSensor(id=3, is_active=True)

    # Register sensors with car park
    car_park.register(entry_sensor)
    car_park.register(exit_sensor)
    car_park.register(temp_sensor)  

    # Simulate vehicles entering
    for _ in range(10):
        entry_sensor.detect_vehicle()

    # Simulates vehicles exiting
    for _ in range(2):
        exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()
