import os
import sys
import discord

from dotenv import load_dotenv

env_files = [f for f in os.listdir() if f.endswith(".env")]
if env_files:
    load_dotenv(env_files[0])

# Path to the terminal
GST_PATH = os.path.join("~", "Documents", "GamestonkTerminal")
sys.path.append(GST_PATH)

# https://discord.com/developers/applications/
DISCORD_BOT_TOKEN = os.getenv("GT_DISCORD_BOT_TOKEN") or "REPLACE_ME"

# https://apidocs.imgur.com
IMGUR_CLIENT_ID = os.getenv("GT_IMGUR_CLIENT_ID") or "REPLACE_ME"

# Settings
COMMAND_PREFIX = "!"
DATE_FORMAT = "%Y-%m-%d"
COLOR = discord.Color.from_rgb(0, 206, 154)
MENU_TIMEOUT = 30

AUTHOR_NAME = "Gamestonk Terminal"
AUTHOR_ICON_URL = (
    "https://github.com/GamestonkTerminal/GamestonkTerminal/"
    "blob/main/images/gst_logo_green_white_background.png?raw=true"
)
