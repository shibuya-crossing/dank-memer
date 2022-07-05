from dank_memer.work import repeat_order

old_message = {
    "contents": """
    Work for Discord Mod - Repeat Order - Remember words order!
    `welcome`
    `moderator`
    `advertising`
    `spam`
    `carl-bot`
    """
}

new_message = {
    "contents": "Click the buttons in correct order!",
    "components": [
        {
            "children": [
                {"label": "advertising"},
                {"label": "moderator"},
                {"label": "carl-bot"},
                {"label": "welcome"},
                {"label": "spam"},
            ]
        }
    ],
}


def test_repeat_order():
    assert repeat_order(old_message, new_message) == [3, 1, 0, 4, 2]
