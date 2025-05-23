# Import the custom decorator and command handler from the core module
from core import Crowthon, handler

# Import the client instance used for sending messages
from clients import crowthon

# Import datetime for latency calculation
from datetime import datetime

# Asynchronous function to load the plugin
async def load_plugin(client):
    # Register a new command handler using the Crowthon decorator
    # Listens for outgoing messages that match the specified pattern (e.g., ".ping")
    @Crowthon(pattern=rf"\{handler}ping")
    async def ping(event):
        # Delete the command message to keep the chat clean
        await event.delete()

        # Define a simple class to measure latency
        class Ping:
            def __init__(self):
                # Start time
                self.start = datetime.now()

                # End time (same as start here)
                self.end = datetime.now()

                # Calculate latency in milliseconds
                self.ms = (self.end - self.start).microseconds / 1000
        
        # Create an instance of the Ping class to measure latency
        server = Ping()

        # Get the chat ID where the command was triggered
        chat = event.to_id

        # Send a response message showing the latency
        await crowthon.send_message(chat, f"Pinged!\nLatency: {server.ms} ms")