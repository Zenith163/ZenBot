import discord
from discord.ext import commands
import sqlite3
from sqlite3 import Error


class feedback(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["fb"])
    # @commands.cooldown(1, 300, commands.BucketType.user)
    async def feedback(self, ctx, *, arg = None):
        if arg == None:
            await ctx.send("Can't send nothing bud")
        else:
            # embed stuff
            embed = discord.Embed()
            embed.set_author(name = ctx.author, icon_url= ctx.author.avatar_url)
            embed.add_field(name = "User ID", value = ctx.author.id, inline = True)
            embed.add_field(name = "Feedback", value = arg, inline = False)
            embed.add_field(name = "Message Link", value = ctx.message.jump_url, inline = False)
            feedback_channel = self.client.get_channel(840975059312181248)
            msg = await feedback_channel.send(embed = embed)
            # database stuff
            db = sqlite3.connect(r"C:\Users\Admin\Desktop\Python Programs\Projects\Zenbot\databases\feedback_database.db")
            cur = db.cursor()
            sql = ("INSERT INTO feedback(user, message_id, message) VALUES(?,?,?)")
            val = (ctx.author.id, msg.id, arg)
            cur.execute(sql, val)
            db.commit()
            cur.close()
            db.close()
            await ctx.send("Feedback submitted")

    @feedback.error
    async def feedback_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timeout = round(error.retry_after, 2)
            await ctx.send(f"You're on cooldown. You can use this command in **{timeout}** seconds")
        else:
            await ctx.send("Please report this error with z.fb along with how you got it")


    # work on feedback resolve command later
    @commands.command(aliases = ["fbr"])
    async def feedbackresolve(self, ctx, *, arg):
        # arg is is message id
        if await self.client.is_owner(ctx.author):
            db = sqlite3.connect(r"C:\Users\Admin\Desktop\Python Programs\Projects\Zenbot\databases\feedback_database.db")
            cursor = db.cursor
            cursor.execute(f"SELECT user FROM feedback WHERE message_id = {arg}")
            result = cursor.fetchone()
            if result == None:
                ctx.send("That feedback doesn't exist")
            else:
                user = result
                await user.send("Feedback Completed")
        else:
            ctx.send("No touchie. For dev only")

def setup(client):
    client.add_cog(feedback(client))