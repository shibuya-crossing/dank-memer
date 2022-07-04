import random
import asyncio
import discord
from datetime import datetime
import os
from dotenv import load_dotenv
import json
from bots.dank.helper import dragon, kraken

from single_acc_parser import start_parser
load_dotenv()

with open("config.json") as f:
    config = json.load(f)
    print("Configuration loaded!")


class Dank(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.channel = config["channels"][kwargs["user"].lower()]
        self.bot_id = "270904126974590976"

    async def setup_hook(self) -> None:
        print("Setting up hook...")
        self.bg_task = self.loop.create_task(self.dank_loop())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        await self.setup_hook()
        print("Hook set up!")

    async def on_message(self, message):
        if str(message.author.id) == self.bot_id and message.channel.id == self.channel:
            print(
                f"{message.author} ({datetime.now().strftime('%d/%m/%y, %I:%M:%S %p')}): {message.content}")
            
            if 'hunting rifle' in message.content:
                await asyncio.sleep(random.randrange(2,4))
                await message.channel.send('pls buy hunting rifle')
            
            if 'shovel' in message.content:
                await asyncio.sleep(random.randrange(2,4))
                await message.channel.send('pls buy shovel')

            if 'fishing pole' in message.content:
                await asyncio.sleep(random.randrange(2,4))
                await message.channel.send('pls buy fishing pole')
                
            if 'catch the fish' in message.content.lower():
                position = kraken(message.content)
                await click_button(self, message, position)
                return
            
            if 'dodge the fireball' in message.content.lower():
                position = dragon(message.content)
                await click_button(self, message, position)
                return

            if len(message.embeds) == 0 and len(message.components) == 0:
                return

            if len(message.components) == 0:
                return

            await click_button(self, message)


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


def message_logger_decorator(func):
    async def wrapper(self, message, *args, **kwargs):

        await func(self, message, *args, **kwargs)
        print(
            f"{self.user} ({datetime.now().strftime('%d/%m/%y, %I:%M:%S %p')}): {message}")
        return
    return wrapper


@message_logger_decorator
async def send_message(self, message, channel=0, *args, **kwargs):
    await asyncio.sleep(random.randrange(7, 10))
    if channel == 0:
        channel = self.channel
    await self.get_channel(channel).send(message)


async def click_button(self, message, index=0, *args, **kwargs):
    if len(message.components) == 0:
        return

    number_of_buttons = len(message.components[0].children)

    if index == 0:
        index = random.randrange(0, number_of_buttons)
    
    retry = 0
    while retry < 4:
        try:
            await asyncio.sleep(1)
            await message.components[0].children[index].click()
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


if __name__ == '__main__':
    main()