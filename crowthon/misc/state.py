from clients import mongodb

# Defines a function to turn off AFK status
def off_afk():
    status = {
        # Identifier key for the AFK status document
        "_id": "afk",

        # Sets the status to 'off'
        "status": "off"
    }

    # Returns the status dictionary
    return status

# Defines a function to turn on AFK status
def on_afk():
    status = {
        # Identifier key for the AFK status document
        "_id": "afk",

        # Sets the status to 'on'
        "status": "on"
    }

    # Returns the status dictionary
    return status

# Retrieves the current AFK status from the MongoDB collection
def afk_status():
    # Access the 'AFK' collection in the MongoDB database
    collection = mongodb["AFK"]

    # Find the document with _id equal to 'afk'
    get_afk_status = collection.find_one(
        {
            "_id": "afk"
        }
    )

    # Return the retrieved AFK status document
    return get_afk_status

# Returns a filter dictionary used to query the AFK document
def filter_afk():
    get_afk = {
        "_id": "afk"
    }

    # Return the filter dictionary
    return get_afk

# Returns an update query to set the AFK status to 'on'
def update_on_afk_status():
    update_status = {
        "$set": {
            "status": "on"
        }
    }

    # Return the update query for setting status to 'on'
    return update_status

# Returns an update query to set the AFK status to 'off'
def update_off_afk_status():
    update_status = {
        "$set": {
            "status": "off"
        }
    }

    # Return the update query for setting status to 'off'
    return update_status