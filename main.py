import os, discord, requests, asyncio

from colorthief import ColorThief
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

class DynamicEmbedBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())

        self.CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
        self.UNIVERSE_ID = "4509896324" # Replace with your Universe ID

    async def fetch_latest_poster_url(self):
        url = f"https://thumbnails.roblox.com/v1/games/icons?universeIds={self.UNIVERSE_ID}&size=150x150&format=png&isCircular=false"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                return data["data"][0].get("imageUrl", None)
        return None

    async def fetch_dominant_color(self, image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            color_thief = ColorThief(image_bytes)
            dominant_color = color_thief.get_color(quality=10)
            return discord.Color.from_rgb(*dominant_color), dominant_color
        return discord.Color.default(), (0, 0, 0)

    async def update_embed(self):
        while True:
            poster_url = await self.fetch_latest_poster_url()
            if poster_url:
                embed_color, rgb_values = await self.fetch_dominant_color(poster_url)

                embed = discord.Embed(
                    title="Roblox Game Updated!",
                    description=f"The embed color and image are dynamically updated.\nRGB: **`{rgb_values}`**",
                    color=embed_color
                )
                embed.set_image(url=poster_url)

                channel = self.get_channel(self.CHANNEL_ID)
                if channel:
                    await channel.send(embed=embed)

            await asyncio.sleep(60)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        self.loop.create_task(self.update_embed())

    async def on_message(self, message):
        if message.author != self.user and self.user.mentioned_in(message):
            embed_color, _ = await self.fetch_dominant_color(await self.fetch_latest_poster_url())

            embed = discord.Embed(
                title="Debug Mode: Embed Color Test",
                description=(
                    "**This is a debugging message.**\n"
                    "Checking if the embed color updates correctly.\n"
                    "If you see this, the bot is running and responding."
                ),
                color=embed_color
            )
            embed.set_footer(text="discord.gg/animelaststand", icon_url=self.user.avatar.url)
            embed.set_thumbnail(url=self.user.avatar.url)
            await message.channel.send(embed=embed)

        await self.process_commands(message)

bot = DynamicEmbedBot()
bot.run(os.getenv("DISCORD_TOKEN"))