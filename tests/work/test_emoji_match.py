from dank_memer.work import emoji_match

class Message:
    pass
class ActionRow:
    pass
class Emoji:
    def __init__(self, name):
        self.name = name
class Button:
    def __init__(self, emoji):
        self.emoji = Emoji(emoji)
      
old_message = Message()
old_message.content = """Work for Discord Mod - Emoji Match - Look at the emoji closely!\n🤔"""

new_message = Message()

      
new_message.content = """What was the emoji?"""
new_message.components = [ActionRow()]
new_message.components[0].children = [Button(emoji="😉"), Button(emoji="😉"),
                                      Button(emoji="🤗"), Button(emoji="😀"),
                                      Button(emoji="😁"), Button(emoji="🤔"),
                                      Button(emoji="😁"), Button(emoji="😉")]


def test_emoji_match():
    assert emoji_match(old_message, new_message) == 5
