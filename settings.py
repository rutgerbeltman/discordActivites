import os

import discord
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_choice, create_permission
from dotenv import load_dotenv

load_dotenv()


def _int(name: str):
    try:
        return int(name)
    except ValueError:
        return name


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD_ID = _int(os.getenv('DISCORD_GUILD_ID'))
DISCORD_GUILD_IDS = [DISCORD_GUILD_ID]
DISCORD_INTENTS = discord.Intents(members=True, presences=True, voice_states=True, guild_messages=True, guilds=True)
DISCORD_COGS = [create_choice(name="discordtogethercommand", value="DiscordTogetherCommand")]
DISCORD_COMMAND_PERMISSION_ROLE = _int(os.getenv('DISCORD_COMMAND_PERMISSION_ROLE'))
DISCORD_COMMAND_PERMISSIONS = {
    DISCORD_GUILD_ID: [create_permission(DISCORD_COMMAND_PERMISSION_ROLE, SlashCommandPermissionType.ROLE, True)]
}
