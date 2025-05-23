# Import the Crowthon decorator and handler symbol from the core module
from core import Crowthon, handler

# Import the main Telethon client
from clients import crowthon

# Import environment variable support
from os import environ

# Import specific RPC error to handle inline sending restrictions
from telethon.errors.rpcerrorlist import ChatSendInlineForbiddenError

# Get the assistant bot username from environment variables
assistant_bot = environ["assistant_bot"]

# Asynchronous function to load the plugin
async def load_plugin(client):
    # Register a new command handler using the Crowthon decorator
    # Listens for outgoing messages that match the specified pattern (e.g., ".help")
    @Crowthon(pattern=rf"\{handler}help")
    async def help(event):
        try:
            # Delete the command message to keep the chat clean
            await event.delete()

            # Get the chat ID where the command was triggered
            chat = event.chat_id

            # Perform an inline query using the assistant bot to get the help menu
            inline_query = await crowthon.inline_query(f"{assistant_bot}", "help")

            # Click the first result (send the inline result to the chat)
            await inline_query[0].click(chat)
        
        # Handle the case where inline messages are disabled in the chat
        except ChatSendInlineForbiddenError:
            get_chat_details = await crowthon.get_entity(int(chat))
            chat_name = get_chat_details.title
            await crowthon.send_message(chat, f"Inline message sending is disabled on {chat_name}, which prevents the Help menu from being displayed in this chat.")
        
        # Silently ignore any other unexpected errors
        except:
            pass