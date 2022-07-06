from dank_memer.work import emoji_match
from discord import Button, Component, ActionRow

class Message:
    pass
class ActionRow:
    pass
class Button:
    def __init__(self, emoji):
        self.emoji = emoji
      
old_message = Message()
old_message.contents = """Work for Discord Mod - Emoji Match - Look at the emoji closely!\n🤔"""

new_message = Message()

      
new_message.contents = """What was the emoji?"""
new_message.components = [ActionRow()]
new_message.components[0].children = [Button(emoji="😉"), Button(emoji="😉"),
                                      Button(emoji="🤗"), Button(emoji="😀"),
                                      Button(emoji="😁"), Button(emoji="🤔"),
                                      Button(emoji="😁"), Button(emoji="😉")]


def test_emoji_match():
    assert emoji_match(old_message, new_message) == 5
