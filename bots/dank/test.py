import re

colon_regex = re.compile(r":(.*):")
mo = colon_regex.findall("""
Work for Discord Mod - Color Match - Match the color to the selected word.
<:Yellow:5037156371> `audit`
<:Marine:9738126571> `discord`
<:White:798351675631> `carl-bot`
""")
print(mo)