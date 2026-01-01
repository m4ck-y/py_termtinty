from .color import Color
from typing import Self


class Tinty:

    def __init__(self):
        self.text = ""

    def BLACK(self, text: str) -> Self:
        self.text += Color.BLACK + text
        return self
    
    def RED(self, text: str) -> Self:
        self.text += Color.RED + text
        return self
    
    def GREEN(self, text: str) -> Self:
        self.text += Color.GREEN + text
        return self
    
    def YELLOW(self, text: str) -> Self:
        self.text += Color.YELLOW + text
        return self
    
    def BLUE(self, text: str) -> Self:
        self.text += Color.BLUE + text
        return self

    def MAGENTA(self, text: str) -> Self:
        self.text += Color.MAGENTA + text
        return self

    def CYAN(self, text: str) -> Self:
        self.text += Color.CYAN + text
        return self

    def RESET(self, text: str) -> Self:
        self.text += Color.RESET + text
        return self
    

    def __str__(self):
        final = self.text + Color.RESET
        self.text = ""
        return final

    def __repr__(self):
        return f"{self.text}"