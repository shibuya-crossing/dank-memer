class Message:
    pass


class ActionRow:
    pass


class Emoji:
    def __init__(self, name):
        self.name = name


class Button:
    def __init__(self, *, label=None, emoji=None):
        self.label = label
        self.emoji = Emoji(emoji)
