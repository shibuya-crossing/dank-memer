from enum import Enum
import re
from utils.utils import count_whitespaces, remove_whitespaces_from_array

# Regex
colon_regex = re.compile(r":(.*):")
tilde_regex = re.compile(r"`(.*)`")

class Work:
    def __init__(self, message):
        self.message = message
        self.minigame = self.get_minigame(message)

    def get_minigame(self):
        if "color match" in self.message_contents:
            return ColorMatch(self.message)
        
        if "soccer" in self.message_contents:
            return self.Minigame(1)

        if "repeat order" in self.message_contents:
            return self.Minigame(2)


    def get_answer(self):
        return 'hi'


class ColorMatch:
    def __init__(self, message) -> None:
        self.text = message.contents.lower()

    @property
    def contents(self):
        options = dict(zip(tilde_regex.findall(self.text), colon_regex.findall(self.text)))

        return {
            "answer": False,
            "options": options
        }

class Soccer:
    def __init__(self, message) -> None:
        self.text = message.contents.lower()

    @property
    def contents(self):
        lines = remove_whitespaces_from_array(self.text.split('\n'))