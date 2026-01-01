from .color import enum_color
from typing import Self


class Tinty:

    def __init__(self):
        self.text = ""

    def BLACK(self, text: str) -> Self:
        self.text += enum_color.BLACK + text
        return self
    
    def RED(self, text: str) -> Self:
        self.text += enum_color.RED + text
        return self
    
    def GREEN(self, text: str) -> Self:
        self.text += enum_color.GREEN + text
        return self
    
    def YELLOW(self, text: str) -> Self:
        self.text += enum_color.YELLOW + text
        return self
    
    def BLUE(self, text: str) -> Self:
        self.text += enum_color.BLUE + text
        return self

    def MAGENTA(self, text: str) -> Self:
        self.text += enum_color.MAGENTA + text
        return self

    def CYAN(self, text: str) -> Self:
        self.text += enum_color.CYAN + text
        return self

    def RESET(self, text: str) -> Self:
        self.text += enum_color.RESET + text
        return self
    

    def __str__(self):
        final = self.text + enum_color.RESET
        self.text = ""
        return final

    def __repr__(self):
        return f"{self.text}"