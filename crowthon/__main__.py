# Import the userbot and bot clients along with the bot token
from clients import crowthon, crowthon_bot, token

# Import glob to dynamically load plugin files
from glob import glob

# Import asyncio utilities for asynchronous operations
from asyncio import sleep, run

# Import signal handling for graceful shutdown
from signal import signal, SIGINT

# Define a function to handle termination signals (e.g., Ctrl+C)
def signal_handler(sig, frame):
    print("\nReceived signal:", sig)
    print("Stopping Crowthon gracefully...")
    crowthon.disconnect() # Disconnect the userbot client
    crowthon_bot.disconnect() # Disconnect the bot client
    exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal(SIGINT, signal_handler)

# Define the main asynchronous function that runs the userbot and bot
async def main():
    # Dynamically load all plugin files from the plugins directory
    for plugin in glob("crowthon/plugins/*.py"):
        plugin_name = plugin.replace(".py", "").replace("crowthon/plugins/", "")
        module = __import__(f"plugins.{plugin_name}", fromlist=[plugin_name])

        # If the plugin has a load_plugin coroutine, load it
        if hasattr(module, "load_plugin"):
            await module.load_plugin(crowthon)
            print(f"{plugin_name} plugin loaded successfully")
    try:
        # Start the userbot client
        await crowthon.start()
        print("Crowthon started successfully")

        # Start the bot client with the provided token
        await crowthon_bot.start(bot_token=token)
        print("Assistant Bot started successfully\n\n")

        # Keep the program running indefinitely
        await sleep(float("inf"))
    except KeyboardInterrupt:
        # Handle Ctrl+C interruption and disconnect clients
        print("\nKeyboardInterrupt received. Stopping Crowthon gracefully...")
        await crowthon.disconnect()

# Run the main coroutine using asyncio's event loop
run(main())