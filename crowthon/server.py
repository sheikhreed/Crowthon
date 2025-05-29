# Import Flask and jsonify to create a web server and return JSON responses
from flask import Flask, jsonify

# Import environ to access environment variables like PORT
from os import environ

# Import Thread to run the Flask server in a separate thread
from threading import Thread

# Create a new Flask web application instance
crowthon = Flask(__name__)

# Handle requests to /favicon.ico to avoid unnecessary errors/logs
@crowthon.route("/favicon.ico")
def favicon():
    # Return an empty response with HTTP status 204 (No Content)
    return "", 204

# Define the root route of the web server
@crowthon.route("/")
def index():
    status = {
        # Name of the project
        "name": "Crowthon",

        # Type of application
        "type": "Userbot",

        # Health status message
        "status": "Alive"
    }

    # Return the status dictionary as a JSON response
    return jsonify(status)

def run_server():
    # Get the PORT from environment variables, default to 8080
    port = int(environ.get("PORT", 8080))

    # Start the Flask server on all available network interfaces
    crowthon.run(host="0.0.0.0", port=port)

def keep_alive():
    # Create a new thread to run the server without blocking the main app
    thread = Thread(target=run_server)

    # Start the Flask server in a background thread
    thread.start()