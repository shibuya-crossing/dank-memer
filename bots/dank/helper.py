from enum import Enum


class Position(Enum):
    Left = 0
    Middle = 1
    Right = 2


kraken_text = [
    """
Catch the fish!
              :Kraken:
:bucket::bucket::bucket: 
""",
    """
Catch the fish!
:legendaryfish:
:bucket::bucket::bucket:
""",
    """
Catch the fish!
       <:legendaryfish:
:bucket::bucket::bucket: 
""",
]

dragon_text = [
    """
Dodge the Fireball
       :Dragon:
              :FireBall:
              :levitate: 
""",
    """
Dodge the Fireball
       :Dragon:
              :FireBall:
:levitate: 
""",
    """
Dodge the Fireball
       :Dragon:
       :FireBall:
       :levitate: 
""",
]


def main():
    # print(dragon(dragon_text[2]))
    print(kraken(kraken_text[2]))


def kraken(message):
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


def count_whitespaces(text):
    for index, char in enumerate(text):
        if char == "<":
            return index


def remove_whitespaces_from_array(array):
    new_array = []
    for i in array:
        if i != "":
            new_array.append(i)

    return new_array


if __name__ == "__main__":
    main()
