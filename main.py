import discord
import json

options = json.load(open('options.json'))

voiceclient = None

class MusicBot(discord.Client):
    async def on_connect(self):
        print("Logging in to discord")
    
    async def on_ready(self):
        print("Logged in as {0.user}".format(client))

        # Set presence
        activity = discord.Game("with Himself")
        await client.change_presence(status=discord.Status.online, activity=activity)

    async def on_resumed(self):
        print("Resumed")

    async def shutdown(self):
        print("Closing connection to Discord...")
        await super().close()

    async def close(self):
        print("Closing on keyboard interrupt...")
        await self.shutdown()

    async def on_disconnect(self):
        print("Bot disconnected.")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("Whos Daryl?"):
            await message.channel.send("Well fuck you too mate")

        if message.content.startswith(">join"):
            await message.channel.send("On the way")
            global voiceclient
            channel = message.author.voice.channel
            voiceclient = await channel.connect()

        if message.content.startswith(">leave"):
            await message.channel.send("Righto mate")
            await voiceclient.disconnect()

        if message.content.startswith(">play"):
            await message.channel.send("Alright cunt, gimme a sec")
            voiceclient.play(discord.FFmpegPCMAudio("vitality.mp3"), after=lambda x: endSong(channel, "vitality.mp3"))
            voiceclient.source = discord.PCMVolumeTransformer(voiceclient.source, 1)

client = MusicBot()
client.run(options['token'])