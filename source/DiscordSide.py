from ReadFiles import ReadFiles
import discord, os

read_file = ReadFiles()
conf_dic = read_file.getDiscordConf()
DISCORD_TOKEN = conf_dic["discord_token"]
channels_dic = read_file.getForwadingConf()
DISCORD_CHANNEL_ID = int(channels_dic[""])

class DiscordClient(discord.Client):

    def __init__(self, message_file_path):
        discord.Client.__init__(self)
        self.MESSAGE_FILE_PATH = message_file_path
        self.read_file = ReadFiles()

    async def on_ready(self):
        while(True):
            if os.path.exists(self.MESSAGE_FILE_PATH):
                message = self.read_file.getFileContent(self.MESSAGE_FILE_PATH)
                await self.discordSendMessage(message)


    async def discordSendMessage(self, message):
        channel = self.get_channel(DISCORD_CHANNEL_ID)
        await channel.send(message)
        print("Message envoyé")
        os.remove(self.MESSAGE_FILE_PATH)

discord_client = DiscordClient("assets/message.txt")
discord_client.run(DISCORD_TOKEN)