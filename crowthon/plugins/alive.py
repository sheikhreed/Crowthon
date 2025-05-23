# Import the custom decorator and command handler from the core module
from core import Crowthon, handler

# Import the client instance used for sending messages
from clients import crowthon

# Import the function that returns the alive status message
from misc import get_alive_text

# Asynchronous function to load the plugin
async def load_plugin(client):
    # Register a new command handler using the Crowthon decorator
    # Listens for outgoing messages that match the specified pattern (e.g., ".alive")
    @Crowthon(pattern=rf"\{handler}alive")
    async def alive(event):
        # Delete the original command message from the user
        await event.delete()

        # Retrieve information about the user who triggered the command
        get_user = await event.get_sender()

        # Extract the user's first name to personalize the response
        first_name = get_user.first_name

        # Generate the alive status message using the first name
        message = get_alive_text(first_name)

        # Get the chat ID where the command was triggered
        chat = event.to_id

        # Send the alive status message to the same chat
        await crowthon.send_message(chat, message)