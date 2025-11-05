class CarPark:
    def __init__ (self, location="Unknown", capacity=0, plates=None, displays=None):
        """
        Initializes a new CarPark object.
        
        Args:
            location (str): Name or address of the car park. Default is "Unknown".
            capacity (int): Total number of parking bays. Default is 0.
            plates (list of str, optional): List to store license plates. Default is empty list.
            displays (list of Display, optional): List of Display objects. Default is empty list.
        """
        self.location = location
        self.display = displays or []
        self.capacity = capacity
        self.plate = plates or []
        
    def __str__ (self):
        """
        Returns a readable string representation of the CarPark object.
        """
        return f"The carpark at {self.location} has {self.capacity} bays"
        
# testing inputs
if __name__ == "__main__":
    location = "Kalamunda"
    capacity = 15
    carpark = CarPark(location, capacity)
    print(carpark)