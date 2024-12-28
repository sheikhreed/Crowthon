from os import environ

try:
    handler = environ["command_handler"]
    if handler == "":
        handler = "."
except KeyError:
    handler = "."
