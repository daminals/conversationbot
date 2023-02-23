# bot.py
# Daniel Kogan
# 02.22.2023

from discord.ext import commands
from dotenv import load_dotenv
import discord, os

intents = discord.Intents.all()
load_dotenv()
TOKEN = os.environ.get('TOKEN', 3)

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# events
import random

@bot.event
async def on_message(message):
  if message.author.bot: # if the message was written by the bot, ignore it
    return
  bot_reactions = ["😎", "😍", "😂", "🥶", "😱", "😳", "🤢", "🥱", "🤐", "🤯", "🤠", "💀", "🤏", "👀", "🌵", "⚡️", "💦", "🎉",
                   "🥳", "😈", "🤡", "✅", "❌", "🤔", "🙄", "🥺", "🤧", "🆗", "💰", "🥰", "😜", "💪", "🤙", "👑", "✈️", "🔪",
                   "😕","👺","🐸","💅","🤦‍♀️","💆‍♀️","🧏‍♀️","💁‍♀️","🤒","🤮","🤥","🤤","😬","😰","🤭","🤫","😓","🥺"]
  # bot_reactions.append(<:reaction_name:id>)
  if (random.randint(0, 100) > 97):
     await message.add_reaction(random.choice(bot_reactions))

  if (len(message.attachments) > 0 or 'https://' in message.content): 
    # if there is a link or attachment in the message add these reactions
    await message.add_reaction('<:upvote:776161705960931399>')
    await message.add_reaction('<:downvote:776162465842200617>')

  if ('happy birthday' in message.content.lower()) and not (message.author.bot):
     # if you included the previous message.author.bot code, you do not need the second part
     # of this conditional statement
     await message.add_reaction("🎉")
     await message.reply("https://tenor.com/view/happy-birthday-the-office-dwight-dwight-schrute-birthday-gif-25725679")

  if ('long island' in message.content.lower()) and not (message.author.bot):
    # send great gatsby text file as attachment
    await message.reply(file=discord.File('gatsby.txt'))

  await bot.process_commands(message) # run all bot commands
  # if you do not include the above command, the bot will not
  # run any of your defined commands

@bot.event
async def on_message_edit(old, message):
  upvote = bot.get_emoji(776161705960931399)
  if (len(message.attachments) > 0 or 'https://' in message.content) and not (upvote in message.reactions):
    # if the message does not have upvote/downvote reactions and
    # contains content, add them
    await message.add_reaction('<:upvote:776161705960931399>')
    await message.add_reaction('<:downvote:776162465842200617>')

@bot.event
async def on_command(ctx):
  await ctx.message.add_reaction('✅')

# end
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)
