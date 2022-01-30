# buildapcsales-discord-bot
### Discord bot that streams the r/buildapcsales subreddit directly to a Discord server channel using Nextcord and Async PRAW.

## Installation/Dependencies
#### Only Python 3.8 or higher is supported.
##### Install the three dependencies using pip
`nextcord` `python-dotenv` `asyncpraw`

```
pip install nextcord python-dotenv asyncpraw
```
#### Register a script application on Reddit [here](https://www.reddit.com/prefs/apps) and note the client ID and client secret keys
#### Create a new bot application on Discord [here](https://discord.com/developers/applications) and note the bot token key & copy the invite link URL to add the bot to your server if needed

### Configure the keys as environment variables in the same directory.
##### .env
```
DISCORD_TOKEN=
CLIENT_ID=
CLIENT_SECRET=
```

## Commands/Usage
- `/setchannel` Sets the channel this command is mentioned in and initializes the feed (must be called again if the feed is stopped)
- `/setchannel stop` Stops the feed

### Bot invite link if needed [here](https://discord.com/api/oauth2/authorize?client_id=935682293207535677&permissions=8&scope=bot).
