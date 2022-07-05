from enum import Enum
from numbers import Number
from .utils import remove_whitespaces_from_array, count_whitespaces


class Position(Enum):
    Left = 0
    Middle = 1
    Right = 2


def kraken(message) -> Number:
    lines = remove_whitespaces_from_array(message.split("\n"))
    kraken_line = lines[1]

    # Calcuwulation
    kraken_pos = Position(count_whitespaces(kraken_line) // 7)
    for pos in Position:
        if pos.value == kraken_pos.value:
            return pos.value


def dragon(message):
    lines = remove_whitespaces_from_array(message.split("\n"))
    dragon_line = lines[1]
    fireball_line = lines[2]
    man_line = lines[3]

    # Calcuwulation
    fireball_pos = Position(count_whitespaces(fireball_line) // 7)
    for pos in Position:
        if pos.name != fireball_pos.name:
            return pos.value
