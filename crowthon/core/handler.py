# Import environment variable handling from the OS module
from os import environ

# Import the function to load variables from a .env file
from dotenv import load_dotenv

# Load environment variables from the .env file into the environment
load_dotenv()

try:
    # Try to get the 'handler' variable from environment
    handler = environ["handler"]

    # If 'handler' is an empty string, default it to "."
    if handler == "":
        handler = "."
except KeyError:
    # If 'handler' is not defined in environment variables, set it to default "."
    handler = "."