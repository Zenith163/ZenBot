import discord
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # add embeds to this stuff
    @commands.command(aliases = ["ui"])
    async def userinfo(self, ctx, member:discord.User = None):
        if member == None:
            await ctx.send(f"**{ctx.author}**\nID: {ctx.author.id}\nCreated at: {ctx.author.created_at}\nAvatar: {ctx.author.avatar_url}")
        else:
            await ctx.send(f"**{member}**\nID: {member.id}\nCreated at: {member.created_at}\nAvatar: {member.avatar_url}")
    
    # add embeds and figure out role permission stuff
    @commands.command(aliases = ["ri"])
    async def roleinfo(self, ctx, role:discord.Role = None):
        if role == None:
            await ctx.send("You must input a role name or id")
        else:
            await ctx.send(f"**{role}**\nId: {role.id}\nMentionable: {role.mentionable}\nPermissions: {role.permissions}\nColor: {role.color}\nCreated at {role.created_at}")

    @commands.command(aliases = ["si", "gi"])
    async def serverinfo(self, ctx, *, guild:discord.Guild = None):
        if guild == None:
            await ctx.send(f"You have to put the name of the server")
        else:
            await ctx.send(f"**{guild}**\nBoosts = {guild.premium_subscription_count}")

    @commands.command
    @commands.has_role(843657026919596123)
    async def sourcecode(self, ctx):
        await ctx.send("https://github.com/Zenith163/Zenbot")

def setup(client):
    client.add_cog(Info(client))