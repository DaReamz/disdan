from discord.ext import commands


exts = ["ai", "sra", "misc"]

async def setup(bot: commands.Bot):
  for ext in exts:
    ext="cogs."+ext
    await bot.load_extension(ext)

async def teardown(bot: commands.Bot):
  for ext in exts:
    ext="cogs."+ext
    await bot.unload_extension(ext)
