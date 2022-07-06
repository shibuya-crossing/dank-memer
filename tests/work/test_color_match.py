from dank_memer.work import color_match
from .test_emoji_match import Message, Button, ActionRow

old_msg = Message()
old_msg.content = """
    **Work for Santa Claus** - Color Match - Match the color to the selected word.
    <:Marine:863886248572878939> `nick`
    <:Black:863886248431190066> `ho`
    <:White:863886248689926204> `elves`
"""

new_msg = Message()
new_msg.content = "What color was next to the word `elves`?"
new_msg.component = [ActionRow()]
new_msg.component[0].children = [Button(label='Cyan'), Button(label='Marine'),
                                 Button(label='White'), Button(label='Black')]

def test_hi():
    assert color_match(old_msg, new_msg) == 2
