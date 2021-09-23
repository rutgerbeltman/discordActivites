from discord.ext import commands
from discordTogether.discordTogetherMain import defaultApplications, DiscordTogether
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

import settings

client = commands.Bot(command_prefix="!", intents=settings.DISCORD_INTENTS)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True, override_type=True)
discordControl = DiscordTogether(client)


@slash.slash(name="activity", description="play activity", guild_ids=settings.DISCORD_GUILD_IDS,
             options=[create_option(name="activity", description="Activity name", option_type=3, required=True, choices=[create_choice(i,i) for i in defaultApplications])])
async def activity(ctx: SlashContext, activity: str):
    if not ctx.author.voice or not ctx.author.voice.channel:
        return await ctx.send("You're not in a voice channel", hidden=True)
    channel = ctx.author.voice.channel
    link = await discordControl.create_link(channel.id, activity)

    await ctx.send(f"Created \"{activity}\" activity in {channel.mention}. Click the link below to activate it.\n{link}")


if __name__ == "__main__":

    client.run(settings.DISCORD_TOKEN)
