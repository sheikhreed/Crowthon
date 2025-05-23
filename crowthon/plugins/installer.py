# Import the custom decorator, command handler and PluginManager class from the core module
from core import Crowthon, handler, PluginManager

# Asynchronous function to load the plugin
async def load_plugin(client):
    # Register a new command handler using the Crowthon decorator
    # Listens for outgoing messages that match the specified pattern (e.g., ".install")
    @Crowthon(pattern=rf"\{handler}install")
    async def plugin_installer(event):
        # Create an instance of PluginManager
        plugin = PluginManager()

        # Call the install_plugin method to handle plugin installation
        await plugin.install_plugin(event)