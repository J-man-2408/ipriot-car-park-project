from io import StringIO
import sys
import unittest
from display import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(id=1, is_on=True)

    def test_update_printed_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output  
        self.display.update({"message": "Goodbye"})
        sys.stdout = sys.__stdout__  
        self.assertIn("Goodbye", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
