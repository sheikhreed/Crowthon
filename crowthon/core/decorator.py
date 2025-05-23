# Import the user Telegram client (with string session) from the clients module
from clients import crowthon

# Import Telethon's event handler for new outgoing messages
from telethon import events

# Define a custom class to act as a decorator for userbot commands
class Userbot:
    def __init__(self, client):
        # Store the provided client (Telethon client) for later use
        self.client = client

    # Make the class instance callable like a decorator
    def __call__(self, pattern):
        # This method will be used as a decorator for functions
        def decorator(func):
            # Register the function to handle outgoing messages matching the pattern
            @self.client.on(events.NewMessage(outgoing=True, pattern=pattern))
            async def wrapper(event):
                # Call the original function with the event
                await func(event)
            return wrapper
        return decorator

# Create an instance of Userbot using the crowthon (user account) client
Crowthon = Userbot(crowthon)