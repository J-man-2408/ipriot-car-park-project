class Display:
    """
    A display to show car park info such as available bays and temperature.
    """
    
    def __init__ (self, id, message="", is_on=False):
        """
        Initialises a display with ID, optional message, and on/off state.
        """
        self.id = id
        self.message=message
        self.is_on=is_on
        
    def update(self, data):
        """
        Update display with data dictionary and print info.
        """
        for key, value in data.items():
            print(f"[Display {self.id}] {key}: {value}")

        
    def __str__ (self):
        """
        Return readable string representation of the display
        """
        return f"Display {self.id}: {self.message}"