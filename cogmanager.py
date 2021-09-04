from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

import settings

client = commands.Bot(command_prefix="!", intents=settings.DISCORD_INTENTS)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True, override_type=True)


@slash.slash(name="load",
             description="load a cog",
             guild_ids=settings.DISCORD_GUILD_IDS,
             permissions=settings.DISCORD_COMMAND_PERMISSIONS,
             default_permission=False,
             options=[
                 create_option(name="cog", description="Select Cog", option_type=3, required=True,
                               choices=settings.DISCORD_COGS)
             ])
async def _load(ctx, cog: str):
    """
    Load a cog
    :param ctx:  slash command context
    :param cog: name of the cog
    :return:
    """
    cog, className = cog.lower(), cog
    try:
        client.load_extension(f"cogs.{cog}")
        # bot = client.get_cog(className)
        # await bot.on_ready()
        await ctx.send(f"Cog: \"{cog}\" loaded.", hidden=True)
    except commands.errors.ExtensionAlreadyLoaded:
        await ctx.send(f"Cog: \"{cog}\" already loaded.", hidden=True)


@slash.slash(name="unload",
             description="unload a cog",
             guild_ids=settings.DISCORD_GUILD_IDS,
             permissions=settings.DISCORD_COMMAND_PERMISSIONS,
             default_permission=False,
             options=[
                 create_option(name="cog", description="Select Cog", option_type=3, required=True,
                               choices=settings.DISCORD_COGS)
             ])
async def _unload(ctx, cog: str):
    """
    Unload a cog
    :param ctx: Original slash command context
    :param cog: Name of the cog to unload
    :return:
    """
    cog, className = cog.lower(), cog
    try:
        client.unload_extension(f"cogs.{cog}")
        await ctx.send(f"Cog: \"{cog}\" unloaded.", hidden=True)
    except commands.errors.ExtensionNotLoaded:
        await ctx.send(f"Cog: \"{cog}\" not loaded.", hidden=True)


@slash.slash(name="reload",
             description="reload a cog",
             guild_ids=settings.DISCORD_GUILD_IDS,
             permissions=settings.DISCORD_COMMAND_PERMISSIONS,
             default_permission=False,
             options=[
                 create_option(name="cog", description="Select Cog", option_type=3, required=True,
                               choices=settings.DISCORD_COGS)
             ])
async def _reload(ctx, cog: str):
    """
    Reload a cog
    :param ctx:  original slash command context
    :param cog: Name of the cog to reload
    :return:
    """
    # Attempt to unload
    cog, className = cog.lower(), cog
    try:
        client.unload_extension(f"cogs.{cog}")
    except commands.errors.ExtensionNotLoaded:
        pass

    # Load the cog
    client.load_extension(f"cogs.{cog}")
    # bot = client.get_cog(className)
    # await bot.on_ready()
    await ctx.send(f"Cog: \"{cog}\" reloaded.", hidden=True)


if __name__ == "__main__":
    # Load all cogs
    for cog in settings.DISCORD_COGS:
        client.load_extension(f'cogs.{cog["name"]}')

    client.run(settings.DISCORD_TOKEN)
