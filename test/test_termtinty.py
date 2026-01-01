import unittest
import re
from termtinty.color import enum_color
from termtinty.text_colored import Tinty

class TestStrColor(unittest.TestCase):

    def setUp(self):
        self.color = Tinty()

    def test_single_colors(self):
        """Verifica que cada color individual genere el código ANSI correcto"""
        colors = {
            "BLACK": enum_color.BLACK,
            "RED": enum_color.RED,
            "GREEN": enum_color.GREEN,
            "YELLOW": enum_color.YELLOW,
            "BLUE": enum_color.BLUE,
            "MAGENTA": enum_color.MAGENTA,
            "CYAN": enum_color.CYAN,
            "RESET": enum_color.RESET,
        }

        for method_name, ansi_code in colors.items():
            c = Tinty()
            method = getattr(c, method_name)
            method("Test")
            output = str(c)
            # Verifica que el código ANSI esté presente
            self.assertIn(ansi_code, output)
            # Verifica que RESET esté al final
            self.assertTrue(output.endswith(enum_color.RESET))
            # Verifica que el texto visible sea correcto
            visible_text = re.sub(r'\x1b\[[0-9;]*m', '', output)
            self.assertEqual(visible_text, "Test")
            # self.text debe resetearse después de str()
            self.assertEqual(c.text, "")

    def test_chain_colors(self):
        """Verifica encadenamiento de colores y reset"""
        self.color.YELLOW("Hola").BLUE(" Mundo").RED("!")
        output = str(self.color)
        # Verifica que todos los códigos ANSI estén presentes
        self.assertIn(enum_color.YELLOW, output)
        self.assertIn(enum_color.BLUE, output)
        self.assertIn(enum_color.RED, output)
        # Verifica que RESET esté al final
        self.assertTrue(output.endswith(enum_color.RESET))
        # Texto visible correcto
        visible_text = re.sub(r'\x1b\[[0-9;]*m', '', output)
        self.assertEqual(visible_text, "Hola Mundo!")
        # self.text debe resetearse
        self.assertEqual(self.color.text, "")

    def test_repr(self):
        """Verifica __repr__ sin reset"""
        self.color.GREEN("Test")
        repr_output = repr(self.color)
        # __repr__ devuelve text sin reset
        self.assertEqual(repr_output, enum_color.GREEN + "Test")
        # self.text aún no se ha reseteado
        self.assertEqual(self.color.text, enum_color.GREEN + "Test")
        # Después de str(), se resetea
        _ = str(self.color)
        self.assertEqual(self.color.text, "")

    def test_reset_behavior(self):
        """Verifica que text se resetea correctamente después de str() y nuevos colores se concatenan"""
        self.color.CYAN("1").MAGENTA("2")
        _ = str(self.color)
        self.assertEqual(self.color.text, "")
        # Nuevo color después de reset
        self.color.BLACK("3")
        self.assertEqual(self.color.text, enum_color.BLACK + "3")

if __name__ == "__main__":
    unittest.main()
