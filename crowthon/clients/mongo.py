# Imports the 'environ' object to access environment variables
from os import environ

# Imports the function to load environment variables from a .env file
from dotenv import load_dotenv

# Imports the MongoClient class to connect to MongoDB
from pymongo import MongoClient

# Loads environment variables from a .env file into the environment
load_dotenv()

# Retrieves the MongoDB connection string from environment variables
connection_string = environ["connection_string"]

# Defines a class named MongoDatabase
class MongoDatabase:
    # Constructor method that runs when an object of this class is created
    def __init__(self):
        # Creates a MongoClient using the connection string
        self.client = MongoClient(connection_string)

        # Connects to the 'Crowthon' database within MongoDB
        self.database = self.client["Crowthon"]

# Creates an instance of the MongoDatabase class
database = MongoDatabase()

# Retrieves the MongoDB database object for further use
mongodb = database.database