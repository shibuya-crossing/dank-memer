import re

import discord
from .helper import kraken, dragon

# Regex
colon_regex = r"(?<=:).+(?=:)"
tilde_regex = r"(?<=`).+(?=`)"


def color_match(old_msg: discord.Message, new_msg: discord.Message):
    colours = re.findall(colon_regex, old_msg.content)
    words = re.findall(tilde_regex, old_msg.content)
    asked = re.search(tilde_regex, new_msg.content).group()

    for c, w in zip(colours, words):
        if w != asked:
            continue
        for btn_idx, btn in enumerate(new_msg.components[0].children):
            if btn.label == c:
                return btn_idx


def emoji_match(old_msg: discord.Message, new_msg: discord.Message):
    # Emoji is located at the end
    emoji = old_msg.content[-1]
    for row_idx, row in enumerate(new_msg.components):
        for btn_idx, btn in enumerate(row.children):
            if btn.emoji.name == emoji:
                return btn_idx + row_idx * 5


def repeat_order(old_msg: discord.Message, new_msg: discord.Message):
    words = re.findall(tilde_regex, old_msg.content)
    order = []
    for word in words:
        for btn_idx, btn in enumerate(new_msg.components[0].children):
            if btn.label == word:
                order.append(btn_idx)
                break

    return order


def soccer(old_msg, new_msg):
    # works the same as dodge the fireball
    return dragon(new_msg)


def dunk_the_ball(old_msg, new_msg):
    # works the same as catch the fish
    # except the ball is in index 2
    return kraken(new_msg, 2)
