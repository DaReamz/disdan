import discord

from discord.ext import commands
from shapesinc import AsyncRoute as Rt
from urllib.parse import urlencode as ufmt
from constant_vars import *
from .img import img_cmd, filter_cmd, tweet_cmd, comment_cmd, mask_cmd, overlay_cmd, anime_cmd



BASE=Rt.__class__("https://api.some-random-api.com/")

class SRA(commands.Cog):
  def __init__(self, bot): self.bot = bot

  async def fetch(self, p: str, params: dict = {}, json=True):
    p=p.lstrip("/") or "/"
    if params: p=p+"?"+ufmt(params)
    return await (BASE/p).request("GET",is_json=json)
    
  urlfmt=staticmethod(ufmt)
  
  async def send_image_embed(self, ctx, url):
    e=discord.Embed(color=EMBED_COLOR)
    e.set_image(url=url)
    return await ctx.reply(embed=e)
    
    
  img=img_cmd
  filter=filter_cmd
  tweet=tweet_cmd
  comment=comment_cmd
  mask=mask_cmd
  overlay=overlay_cmd
  animu=anime_cmd

async def setup(bot: commands.Bot):
  await bot.add_cog(SRA(bot))
  
async def teardown(bot: commands.Bot):
  await bot.remove_cog("SRA")
