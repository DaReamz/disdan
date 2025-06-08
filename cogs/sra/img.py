from discord.ext import commands
import discord
from constant_vars import *
from typing import Optional

class export:
  @commands.command(aliases=["image"])
  async def img(self, ctx, of: str = ""):
    opts=['fox', 'cat', 'birb', 'panda', 'red_panda', 'pikachu', 'racoon', 'koala', 'kangaroo', 'whale', 'dog', 'bird']
    of=of.lower()
    if (not of) or of not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )

    return await self.send_image_embed(ctx, (await self.fetch("img/"+of))["link"]
    )
  @commands.command(aliases=["anime"])
  async def animu(self, ctx, content: str = ""):
    opts=['nom', 'poke', 'cry', 'kiss', 'pat', 'hug', 'wink', 'facepalm', 'quote', 'face-palm']
    of=content.lower().replace("facepalm", "face-palm")
    if (not of) or of not in opts:
      opts.remove('face-palm')
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )

    res=await self.fetch("animu/"+of)
    if of!="quote":
      return await self.send_image_embed(ctx, res["link"])
      
    e=discord.Embed(
      title=res["anime"],
      description=res["name"]+": "+res["quote"],
      color=EMBED_COLOR
    )
    return await ctx.reply(embed=e)
    
  
  @commands.command(name="filter")
  async def filter_cmd(self, ctx, filter: str = "", user: discord.User = None):
    opts="blue blurple pixelate blur blurple2 green greyscale invert red invertgreyscale sepia".split(" ")
    filter=filter.lower().replace("gray", "grey")
    if (not filter) or filter not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )
    im=""
    if user and user.avatar:
      im=user.avatar.url
    if im:...
    elif ctx.message.attachments:
      for m in ctx.message.attachments:
        if m.content_type=="image/png":
          im=m.url
          break
      if not im:
        return await ctx.reply("Only png format is supported!")
    elif ctx.author.avatar and ctx.author.avatar.url:
      im=ctx.author.avatar.url
      
    if not im:
      return await ctx.reply('Couldnt find an image!')
      
    return await self.send_image_embed(ctx, "https://api.some-random-api.com/canvas/filter/"+filter+"?"+self.urlfmt(dict(avatar=im)))
    
  @commands.command(name="overlay")
  async def overlay_cmd(self, ctx, overlay: str = "", user: discord.User = None):
    opts="comrade glass jail passed triggered wasted".split(" ")
    overlay=overlay.lower()
    if (not overlay) or overlay not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )
    im=""
    if user and user.avatar:
      im=user.avatar.url
    if im:...
    elif ctx.message.attachments:
      for m in ctx.message.attachments:
        if m.content_type=="image/png":
          im=m.url
          break
      if not im:
        return await ctx.reply("Only png format is supported!")
    elif ctx.author.avatar and ctx.author.avatar.url:
      im=ctx.author.avatar.url
      
    if not im:
      return await ctx.reply('Couldnt find an image!')
      
    return await self.send_image_embed(ctx, "https://api.some-random-api.com/canvas/overlay/"+overlay+"?"+self.urlfmt(dict(avatar=im)))
    
  @commands.command(name="mask")
  async def mask_cmd(self, ctx, mask: str = "", user: discord.User = None):
    opts="circle heart horny lied lolice simpcard tonikawa".split(" ")
    mask=mask.lower()
    if (not mask) or mask not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )
    im=""
    if user and user.avatar:
      im=user.avatar.url
    if im:...
    elif ctx.message.attachments:
      for m in ctx.message.attachments:
        if m.content_type=="image/png":
          im=m.url
          break
      if not im:
        return await ctx.reply("Only png format is supported!")
    elif ctx.author.avatar and ctx.author.avatar.url:
      im=ctx.author.avatar.url
      
    if not im:
      return await ctx.reply('Couldnt find an image!')
      
    return await self.send_image_embed(ctx, "https://api.some-random-api.com/canvas/misc/"+mask+"?"+self.urlfmt(dict(avatar=im)))
    
  @commands.command()
  async def tweet(self, ctx, *tweet: str):
    tweet=" ".join(tweet)
    return await self.send_image_embed(ctx, "https://api.some-random-api.com/canvas/misc/tweet?"+self.urlfmt(dict(
      displayname=ctx.author.display_name,
      username=ctx.author.name,
      comment=tweet,
      avatar=ctx.author.avatar.url,
      theme="dark"
    )))
    
  @commands.command()
  async def comment(
    self,
    ctx,
    user: Optional[discord.User],
    *,
    comment: str
  ):
    user = user or ctx.author
    return await self.send_image_embed(ctx, "https://api.some-random-api.com/canvas/misc/youtube-comment?"+self.urlfmt(dict(
      username=user.name,
      comment=comment,
      avatar=user.avatar.url,
      theme="dark"
    )))
    
img_cmd=export.img
mask_cmd=export.mask_cmd
filter_cmd = export.filter_cmd
tweet_cmd = export.tweet
comment_cmd = export.comment
overlay_cmd = export.overlay_cmd
anime_cmd = export.animu
