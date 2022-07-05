from enum import Enum
import re

# Regex
colon_regex = re.compile(r":(.*):")
tilde_regex = re.compile(r"`(.*)`")


def color_match(old_msg, new_msg):
    msg = old_msg
    msg.contents = msg.contents.lower()
    words_color = dict(
        zip(tilde_regex.findall(msg.contents), colon_regex.findall(msg.contents))
    )


def emoji_match(old_msg, new_msg):
    return "TODO"


def repeat_order(old_msg, new_msg):
    words = tilde_regex.findall(old_msg["contents"])
    print(words)
    # words = tilde_regex.findall(old_msg.contents)
    order = []
    for _, word in enumerate(words):
        for btn_idx, btn in enumerate(new_msg["components"][0]["children"]):
            # for btn_idx, btn in enumerate(new_msg.components[0].children):
            # if btn.label == word:
            if btn["label"] == word:
                order.append(btn_idx)
                break

    return order


def soccer(old_msg, new_msg):
    return
