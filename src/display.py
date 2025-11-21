class Display:
    def __init__ (self, id, message="", is_on=False):
        self.id = id
        self.message=message
        self.is_on=is_on
        
    def update(self):
        print(f"[Display {self.id}] {self.message}")
        
    def __str__ (self):
        return f"Display {self.id}: {self.message}"