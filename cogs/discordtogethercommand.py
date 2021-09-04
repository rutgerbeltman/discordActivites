from discord.ext import commands
from discord_slash import SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice
from discordTogether import DiscordTogether
from discordTogether.discordTogetherMain import defaultApplications
import settings


class DiscordTogetherCommand(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.discordControl = DiscordTogether(client)

    @cog_ext.cog_slash(name="activity", description="play activity", guild_ids=settings.DISCORD_GUILD_IDS,
                       options=[create_option(name="activity", description="Activity name", option_type=3, required=True, choices=[create_choice(i,i) for i in defaultApplications])])
    async def activity(self, ctx: SlashContext, activity: str):
        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send("You're not in a voice channel", hidden=True)
        channel = ctx.author.voice.channel
        link = await self.discordControl.create_link(channel.id, activity)

        await ctx.send(f"Created \"{activity}\" activity in {channel.mention}. Click the link below to activate it.\n{link}")

def setup(client):
    client.add_cog( DiscordTogetherCommand(client))
