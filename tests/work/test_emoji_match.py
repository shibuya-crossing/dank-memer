from dank_memer.work import emoji_match
from .mock import Message, ActionRow, Button

old_message = Message()
old_message.content = (
    """Work for Discord Mod - Emoji Match - Look at the emoji closely!\nš¤"""
)

new_message = Message()


new_message.content = """What was the emoji?"""
new_message.components = [ActionRow()]
new_message.components[0].children = [
    Button(emoji="š"),
    Button(emoji="š"),
    Button(emoji="š¤"),
    Button(emoji="š"),
    Button(emoji="š"),
    Button(emoji="š¤"),
    Button(emoji="š"),
    Button(emoji="š"),
]


def test_emoji_match():
    assert emoji_match(old_message, new_message) == 5
