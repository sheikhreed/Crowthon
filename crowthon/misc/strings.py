# Import the current version of Crowthon from the __version__ module
from __version__ import __version__

# Import the Telethon library to get its version
from telethon import version

# Import function to retrieve the current Python interpreter version
from platform import python_version

# Define a function to generate the alive status message using user's first name
def get_alive_text(first_name):
    # Construct the alive status message
    alive_text = (
        f"Hello {first_name},\nFully operational, ever alert, and ready to assist you. "
        "Crafted with code and powered by logic, I watch the stream of commands with unwavering focus.\n\n"
        f"Crowthon: {__version__}\n"
        f"Telethon: {version.__version__}\n"
        f"Python: {python_version()}\n\n"
        "Thank you"
    )

    # Return the composed alive message
    return alive_text

# Define a function to generate the system category help text
def system_menu_text():
    # Create a formatted string containing the bot name, version, and category description
    system_text = (
        f"Crowthon\nVersion: {__version__}\nCategory: System\n\n"
        "The usage of all features in the System category is documented here."
    )

    # Return the generated help text
    return system_text

# Define a function that generates an AFK notification message with the user's first name
def afk_text(first_name):
    # Create a personalized AFK message using the provided first name
    notification = (
        f"Hey {first_name},\n"
        "I'm currently AFK and might not respond right away. "
        "I'll get back to you as soon as I'm available."
    )

    # Return the generated message
    return notification