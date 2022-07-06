from dank_memer.work import repeat_order
from .test_emoji_match import Message, ActionRow, Button


old_message = Message()
old_message.content = """
    Work for Discord Mod - Repeat Order - Remember words order!
    `welcome`
    `moderator`
    `advertising`
    `spam`
    `carl-bot`
"""

new_message = Message()
new_message.components = [ActionRow()]
new_message.components[0].children = [
    Button(label="advertising"),
    Button(label="moderator"),
    Button(label="carl-bot"),
    Button(label="welcome"),
    Button(label="spam"),
]
new_message.content = "Click the buttons in correct order!"


def test_repeat_order():
    assert repeat_order(old_message, new_message) == [3, 1, 0, 4, 2]
