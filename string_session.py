# Used to interact with Telegram synchronously
from telethon.sync import TelegramClient

# Used to generate and save a string session
from telethon.sessions import StringSession

# Used to execute system-level commands like clearing the terminal
from os import system 

# Define a class to handle the generation of a String Session
class Generate:
    def __init__(self):
        # Prompt the user to input their Telegram API ID and convert it to integer
        self.api_id = int(input("Enter App API ID: "))

        # Prompt the user to input their Telegram API Hash
        self.api_hash = input("Enter App API Hash: ")

        # Create a TelegramClient session using the provided API credentials
        with TelegramClient(StringSession(), self.api_id, self.api_hash) as crowthon:
            # Save the string session and send it to the user's Saved Messages
            crowthon.send_message("me", crowthon.session.save())

            # Clear the terminal screen (for Unix-like systems)
            system("clear")

            # Print confirmation message after successful generation
            print(
                "Dear Crowthon user,\n"
                "We are pleased to inform you that your String Season Generation has been successfully completed. "
                "Please check your saved messages chat on Telegram. Your generated String Season has been sent to you there.\n\n"
                "Sincerely,\n"
                "Crowthon"
            )

# Instantiate the Generate class to run the session generation process
string_session = Generate()