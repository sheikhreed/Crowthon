from os import environ

try:
    handler = environ["command_handler"]
except KeyError:
    handler = "."