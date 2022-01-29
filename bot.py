import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands, tasks
import asyncpraw

load_dotenv()

reddit = asyncpraw.Reddit(
client_id = os.getenv("CLIENT_ID"),
client_secret = os.getenv("CLIENT_SECRET"),
user_agent="buildapcsales-discord-bot-v0.1"
)

def main():
    client = commands.Bot(command_prefix='/')

    @client.event
    async def on_ready():
        print("Connected")

    @client.command()
    async def setchannel(ctx, enabled="start"):
        if enabled.lower() == "stop":
            fetch_reddit.cancel()
        elif enabled.lower() == "start":
            fetch_reddit.start(ctx)

    @tasks.loop(seconds=30)
    async def fetch_reddit(ctx):
        subreddit = await reddit.subreddit("all")
        async for submission in subreddit.stream.submissions(skip_existing=True):
            await ctx.send(submission.title)

    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()
