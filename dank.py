import random
import asyncio
import discord
from datetime import datetime
import os
from dotenv import load_dotenv
import json
from dank_memer.helper import dragon, kraken
from dank_memer.acc_parser import start_parser
from dank_memer.work import (
    color_match,
    emoji_match,
    soccer,
    dunk_the_ball,
    repeat_order,
)

# Load environment variables
load_dotenv()

from colorama import Fore, Style

print(
    Fore.MAGENTA
    + """
      _     _ _                       
     | |   (_) |                      
  ___| |__  _| |__  _   _ _   _  __ _ 
 / __| '_ \| | '_ \| | | | | | |/ _` |
 \__ \ | | | | |_) | |_| | |_| | (_| |
 |___/_| |_|_|_.__/ \__,_|\__, |\__,_|
                           __/ |      
                          |___/       
"""
)
print(Style.RESET_ALL)

# Load config
with open("config.json") as f:
    config = json.load(f)
    print("Configuration loaded!")


class Dank(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.channel = (
            config["channels"][kwargs["user"].lower()]
            if kwargs["user"].lower() in config["channels"].keys()
            else config["channels"]["default"]
        )
        # Dank memer bot id
        self.bot_id = "270904126974590976"

    async def setup_hook(self) -> None:
        print("Setting up hook...")
        self.bg_task = self.loop.create_task(self.dank_loop())

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        await self.setup_hook()
        print("Hook set up!")

    async def on_message(self, message):
        if str(message.author.id) == self.bot_id and message.channel.id == self.channel:
            print(
                f"{message.author} ({datetime.now().strftime('%d/%m/%y, %I:%M:%S %p')}): {message.content}"
            )

            if "hunting rifle" in message.content:
                await asyncio.sleep(random.randrange(2, 4))
                await message.channel.send("pls buy hunting rifle")

            if "shovel" in message.content:
                await asyncio.sleep(random.randrange(2, 4))
                await message.channel.send("pls buy shovel")

            if "fishing pole" in message.content:
                await asyncio.sleep(random.randrange(2, 4))
                await message.channel.send("pls buy fishing pole")

            if "catch the fish" in message.content.lower():
                position = kraken(message.content)
                await click_button(self, message, position)
                return

            if "dodge the fireball" in message.content.lower():
                position = dragon(message.content)
                await click_button(self, message, position)
                return

            if len(message.embeds) == 0 and len(message.components) == 0:
                return

            if len(message.components) == 0:
                return

            await click_button(self, message)

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if str(before.author.id) == self.bot_id and before.channel.id == self.channel:
            if "color match" in before.content.lower():
                await click_button(self, after, color_match(before, after))

            if "emoji match" in before.content.lower():
                await click_button(self, after, emoji_match(before, after))

            if "repeat order" in before.content.lower():
                order = repeat_order(before, after)
                for idx in order:
                    await click_button(self, after, idx)

            if "soccer" in before.content.lower():
                await click_button(self, after, soccer(before.content, after.content))

            if "dunk the ball" in before.content.lower():
                await click_button(
                    self, after, dunk_the_ball(before.content, after.content)
                )

    async def dank_loop(self):
        print("Readying...")
        await self.wait_until_ready()
        print("Ready!")
        while not self.is_closed():
            await send_message(self, "pls beg")
            await send_message(self, "pls hunt")
            await send_message(self, "pls fish")
            await send_message(self, "pls dig")
            await send_message(self, "pls hl")
            await send_message(self, "pls search")
            await send_message(self, "pls trivia")
            await send_message(self, "pls pm")
            await send_message(self, "pls work")


def message_logger_decorator(func):
    async def wrapper(self, message, *args, **kwargs):

        await func(self, message, *args, **kwargs)
        print(
            f"{self.user} ({datetime.now().strftime('%d/%m/%y, %I:%M:%S %p')}): {message}"
        )
        return

    return wrapper


@message_logger_decorator
async def send_message(self, message, channel=0, *args, **kwargs):
    await asyncio.sleep(random.randrange(7, 10))
    if channel == 0:
        channel = self.channel
    await self.get_channel(channel).send(message)


async def click_button(self, message, index=None, retries=4, *args, **kwargs):
    if len(message.components) == 0:
        return

    cmp_idx = 0
    if index:
        cmp_idx = index // 5
        index %= 5
    number_of_buttons = len(message.components[cmp_idx].children)

    if index == None:
        index = random.randrange(0, number_of_buttons)

    retry = 0
    while retry < retries:
        try:
            await asyncio.sleep(1)
            await message.components[cmp_idx].children[index].click()
            retry += 1
        except Exception as e:
            print(f"error: {e}")
            retry += 1
            continue
        break


def main():
    parser = start_parser()
    args = parser.parse_args()

    user = args.user.upper()
    if args.token:
        token = args.token
    elif args.user:
        token = os.getenv(user)

    client = Dank(user=user)
    client.run(token)


if __name__ == "__main__":
    main()
