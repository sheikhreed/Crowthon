# Import the crowthon_bot client instance
from clients import crowthon_bot

# Import environment variable
from os import environ

# Import event handling utilities from Telethon
from telethon import events

# Import various menu layouts and utility functions from the misc module
from misc import categories_menu, system_menu, system_menu_text, return_to_the_system_menu

# Import the current version of Crowthon from the __version__ module
from __version__ import __version__

# Import functions from os.path to work with file and directory paths
from os.path import dirname, join, abspath

# Get the owner's user ID from environment variables and convert it to integer
owner = int(environ["owner"])

# Register a callback query event handler for the Crowthon bot
@crowthon_bot.on(events.CallbackQuery)
async def query_response(event):
    try:
        # Get the user ID of the person who triggered the callback
        user_id = event.original_update.user_id

        # Get the data from the button that was pressed
        button_data = event.data

        # Check if the user is the owner of the bot
        if user_id == owner:
            # If the "Account" button was pressed
            if button_data == b'account':
                await event.answer("This feature is not fully implemented yet. Please wait for a future update.", alert=True)
            
            # If the "Group" button was pressed
            elif button_data == b'group':
                await event.answer("This feature is not fully implemented yet. Please wait for a future update.", alert=True)

            # If the "System" button was pressed
            elif button_data == b'system':
                menu_info =  system_menu_text()
                await event.edit(menu_info, buttons=system_menu)
            
            # If the "Alive" button was pressed
            elif button_data == b'alive':
                current_dir = dirname(__file__)
                alive_md_path = join(current_dir, '..', 'docs', 'alive.md')
                alive_md_path = abspath(alive_md_path)
                with open(alive_md_path, 'r') as file:
                    usage = file.read()
                await event.edit(usage, buttons=return_to_the_system_menu, parse_mode="markdown")
            
            # If the "Ping" button was pressed
            elif button_data == b'ping':
                current_dir = dirname(__file__)
                ping_md_path = join(current_dir, '..', 'docs', 'ping.md')
                ping_md_path = abspath(ping_md_path)
                with open(ping_md_path, 'r') as file:
                    usage = file.read()
                await event.edit(usage, buttons=return_to_the_system_menu, parse_mode="markdown")
            
            # If the "Back(System)" button was pressed
            elif button_data == b'back_to_the_system':
                menu_info =  system_menu_text()
                await event.edit(menu_info, buttons=system_menu)
            
            # If the "Main Menu" button was pressed
            elif button_data == b'main_menu':
                await event.edit(f"Crowthon\nVersion: {__version__}\n\nCrowthon's user manual is comprehensive, and the usage of all features is thoroughly documented here.", buttons=categories_menu)
        else:
            # Notify non-owner users that they are not authorized
            await event.answer("You do not have permission to access this resource. To proceed, you need to deploy your own Crowthon.", alert=True)
            
    # Silently ignore any unexpected errors
    except:
        pass