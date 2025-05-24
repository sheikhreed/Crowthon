# Import Crowthon (outgoing message decorator), Croweye (incoming), and handler symbol
from core import Crowthon, Croweye, handler

# Import userbot client and MongoDB connection
from clients import crowthon, mongodb

# Import AFK-related utility functions and state managers
from misc import (
    on_afk, off_afk, afk_status, filter_afk,
    update_on_afk_status, update_off_afk_status, afk_text
)

# Import environment variable to get owner's Telegram ID
from os import environ

# Convert owner ID to integer
owner = int(environ["owner"])

# Asynchronous function to load the plugin
async def load_plugin(client):
    # Register a new command handler using the Crowthon decorator
    # Listens for outgoing messages that match the specified pattern (e.g., ".afk on/off")
    @Crowthon(pattern=rf"\{handler}afk")
    async def afk(event):
        # Delete the original command message from the user
        await event.delete()

        # Get the chat ID where the command was triggered
        chat = event.chat_id

        # Split the raw text of the command into parts
        get_status = event.message.raw_text.split()

        # Count the number of parts in the command
        command_length = len(get_status)

        # Reference the "AFK" collection in MongoDB
        collection = mongodb["AFK"]

        # Check if the command has exactly two parts
        if command_length == 2:
            # Convert the second word to lowercase (on/off)
            command = get_status[1].lower()

            # If the command is either "on" or "off"
            if command in ["on", "off"]:
                # Get current AFK status from the database
                current = afk_status()

                # Handle "on" command
                if command == "on":
                    # If AFK is already on
                    if current and current.get("status") == "on":
                        # Notify already ON
                        await crowthon.send_message(chat, "AFK is already ON")
                    
                    # If AFK exists but not ON
                    elif current:
                        # Update status to ON
                        collection.update_one(filter_afk(), update_on_afk_status())

                        # Notify turned ON
                        await crowthon.send_message(chat, "AFK turned ON")
                    
                    # If AFK document doesn't exist
                    else:
                        # Create a new AFK ON status
                        collection.insert_one(on_afk())

                        # Notify new entry
                        await crowthon.send_message(chat, "AFK ON status created")
                
                # Handle "off" command
                elif command == "off":
                    # If AFK is already off
                    if current and current.get("status") == "off":
                        # Notify already OFF
                        await crowthon.send_message(chat, "AFK is already OFF")
                    
                    # If AFK exists but not OFF
                    elif current:
                        # Update status to OFF
                        collection.update_one(filter_afk(), update_off_afk_status())

                        # Notify turned OFF
                        await crowthon.send_message(chat, "AFK turned OFF")
                    
                    # If AFK document doesn't exist
                    else:
                        # Create a new AFK OFF status
                        collection.insert_one(off_afk())

                        # Notify new entry
                        await crowthon.send_message(chat, "AFK OFF status created")
            
            # Notify invalid second word
            else:
                await crowthon.send_message(chat, "Invalid argument")
        
        # Notify command format is wrong
        else:
            await crowthon.send_message(chat, "Invalid command")

# Listen to all private incoming messages and reply if AFK is on
@Croweye()
async def afk_notification(event):
    # Check if the message is from a private chat
    if event.is_private:
        # Get the sender's full user object
        get_sender = await event.get_sender()

        # Extract the sender's Telegram ID
        sender_id = get_sender.id

        # Get the chat info (can be used for name, type, etc.)
        get_chat = await event.get_chat()

        # Get sender's first name
        first_name = get_chat.first_name

        # Check if the sender is a bot
        is_bot = get_chat.bot

        # Telegram service ID
        telegram = 777000

        # Fetch the current AFK status
        current = afk_status()

        # Check if AFK is turned on
        if current and current.get("status") == "on":
            # Do not respond if the message is from the owner
            if sender_id == owner:
                pass

            # Do not respond to Telegram system messages
            elif sender_id == telegram:
                pass

            # Do not respond to bots
            elif is_bot:
                pass

            # Send AFK reply to all other private users
            else:
                await crowthon.send_message(sender_id, afk_text(first_name))