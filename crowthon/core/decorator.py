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

# Define a class called Watcher to act as a decorator wrapper
class Watcher:
    # Constructor method to initialize the class with a Telethon client
    def __init__(self, client):
        self.client = client

    # Make the class instance callable like a decorator
    def __call__(self):
        # Inner decorator function that takes the target function
        def decorator(func):
            # Register the function as a handler for all new incoming messages
            @self.client.on(events.NewMessage())
            async def wrapper(event):
                # Call the original function with the event object
                await func(event)
            
            # Return the wrapped handler function
            return wrapper
        
        # Return the decorator itself
        return decorator

# Create an instance of Userbot using the crowthon (user account) client
Crowthon = Userbot(crowthon)

# Create an instance of the Watcher decorator for all incoming messages
Croweye = Watcher(crowthon)