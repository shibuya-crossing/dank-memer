from enum import Enum
from numbers import Number
from .utils import remove_whitespaces_from_array, count_whitespaces


class Position(Enum):
    Left = 0
    Middle = 1
    Right = 2


def kraken(message, index=1) -> Number:
    lines = remove_whitespaces_from_array(message.split("\n"))
    kraken_line = lines[index]

    # Calcuwulation
    kraken_pos = Position(count_whitespaces(kraken_line) // 7)
    for pos in Position:
        if pos.value == kraken_pos.value:
            return pos.value


def dragon(message, index=2):
    lines = remove_whitespaces_from_array(message.split("\n"))
    fireball_line = lines[index]

    # Calcuwulation
    fireball_pos = Position(count_whitespaces(fireball_line) // 7)
    for pos in Position:
        if pos.name != fireball_pos.name:
            return pos.value
