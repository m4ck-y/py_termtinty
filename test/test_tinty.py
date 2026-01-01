import unittest
import re
from termtinty.color import Color
from termtinty.tinty import Tinty

class TestStrColor(unittest.TestCase):

    def setUp(self):
        self.color = Tinty()

    def test_single_colors(self):
        """Verifies that each individual color generates the correct ANSI code"""
        colors = {
            "BLACK": Color.BLACK,
            "RED": Color.RED,
            "GREEN": Color.GREEN,
            "YELLOW": Color.YELLOW,
            "BLUE": Color.BLUE,
            "MAGENTA": Color.MAGENTA,
            "CYAN": Color.CYAN,
            "RESET": Color.RESET,
        }

        for method_name, ansi_code in colors.items():
            c = Tinty()
            method = getattr(c, method_name)
            method("Test")
            output = str(c)
            # Verify ANSI code is present
            self.assertIn(ansi_code, output)
            # Verify RESET is at the end
            self.assertTrue(output.endswith(Color.RESET))
            # Verify visible text is correct
            visible_text = re.sub(r'\x1b\[[0-9;]*m', '', output)
            self.assertEqual(visible_text, "Test")
            # self.text should be reset after str()
            self.assertEqual(c.text, "")

    def test_chain_colors(self):
        """Verifies method chaining and reset"""
        self.color.YELLOW("Hola").BLUE(" Mundo").RED("!")
        output = str(self.color)
        # Verify all ANSI codes are present
        self.assertIn(Color.YELLOW, output)
        self.assertIn(Color.BLUE, output)
        self.assertIn(Color.RED, output)
        # Verify RESET is at the end
        self.assertTrue(output.endswith(Color.RESET))
        # Correct visible text
        visible_text = re.sub(r'\x1b\[[0-9;]*m', '', output)
        self.assertEqual(visible_text, "Hola Mundo!")
        # self.text should be reset
        self.assertEqual(self.color.text, "")

    def test_repr(self):
        """Verifies __repr__ without reset"""
        self.color.GREEN("Test")
        repr_output = repr(self.color)
        # __repr__ returns text without reset
        self.assertEqual(repr_output, Color.GREEN + "Test")
        # self.text has not been reset yet
        self.assertEqual(self.color.text, Color.GREEN + "Test")
        # After str(), it resets
        _ = str(self.color)
        self.assertEqual(self.color.text, "")

    def test_reset_behavior(self):
        """Verifies text resets correctly after str() and new color concatenations"""
        self.color.CYAN("1").MAGENTA("2")
        _ = str(self.color)
        self.assertEqual(self.color.text, "")
        # New color after reset
        self.color.BLACK("3")
        self.assertEqual(self.color.text, Color.BLACK + "3")

if __name__ == "__main__":
    unittest.main()
