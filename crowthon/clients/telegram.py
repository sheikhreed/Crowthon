# Import environment variable handling and dotenv support
from os import environ
from dotenv import load_dotenv

# Import Telethon client libraries
from telethon import TelegramClient
from telethon.sessions import StringSession

# Import the current version of Crowthon from the __version__ module
from __version__ import __version__

# Load environment variables from a .env file
load_dotenv()

# Define the Crowthon class to manage both user and bot clients
class Crowthon:
    def __init__(self):
        # Get API ID (integer) from environment variables
        self.api_id = int(environ["api_id"])

        # Get API hash from environment variables
        self.api_hash = environ["api_hash"]

        # Get string session for the user account
        self.string_session = environ["string_session"]

        # Get bot token from environment variables
        self.bot_token = environ["bot_token"]

        # Initialize the user client using StringSession
        self.account = TelegramClient(
            StringSession(self.string_session),
            self.api_id,
            self.api_hash,
            device_model= "Crowthon",
            app_version= __version__
        )

        # Initialize the bot client using a session name "crowthon"
        self.bot = TelegramClient(
            "crowthon",
            self.api_id,
            self.api_hash
        )

# Create an instance of the Crowthon class
client = Crowthon()

# Access the user client from the class
crowthon = client.account

# Get the bot token from the class instance
token = client.bot_token

# Access the bot client from the class
crowthon_bot = client.bot