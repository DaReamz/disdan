import discord
from discord.ext import commands


class HelpCommand(commands.MinimalHelpCommand):
  def __init__(self, **options):
    self.options = options
    self.embed_template = options.get("embed_template", discord.Embed) or discord.Embed
    if not issubclass(self.embed_template, discord.Embed):
      raise TypeError(f"Embed template must be a subclass of discord.Embed not {self.embed_template!r}")
    super().__init__(**options)
    
  async def send_pages(self):
    channel = self.get_destination()
    embeds = []
    for page in self.paginator.pages:
      e = self.embed_template(description=page)
      if self.options.get("color"):
      	e.color=self.options.get("color")
      embeds.append(e)
    for embed in embeds:
      await channel.send(embeds=embeds)

class Misc(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bot.help_command.cog = self

async def setup(bot):
  await bot.add_cog(Misc(bot))

async def teardown(bot):
  bot.help_command.cog = None
  await bot.remove_cog("Misc")
