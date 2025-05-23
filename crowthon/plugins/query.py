# Import the crowthon_bot client instance
from clients import crowthon_bot

# Import event handling utilities from Telethon
from telethon import events

# Import the current version of Crowthon from the __version__ module
from __version__ import __version__

# Import the predefined inline button layout
from misc import categories_menu

# Inline query handler for the assistant bot
@crowthon_bot.on(events.InlineQuery)
async def get_query(query):
    try:
        # Respond only to the "help" inline query
        if query.text == "help":
            # Build an inline article response
            build_article = query.builder.article(
                title = "Crowthon",
                text = f"Crowthon\nVersion: {__version__}\n\nCrowthon's user manual is comprehensive, and the usage of all features is thoroughly documented here.",
                buttons = categories_menu
            )
            # Send the inline result back to the user
            await query.answer([build_article])
    
    # Silently ignore any unexpected errors
    except:
        pass