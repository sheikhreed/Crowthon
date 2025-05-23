# Import the custom decorator, command handler and PluginManager class from the core module
from core import Crowthon, handler, PluginManager

# Asynchronous function to load the plugin
async def load_plugin(client):
    @Crowthon(pattern=rf"\{handler}uninstall")
    # Register a new command handler using the Crowthon decorator
    # Listens for outgoing messages that match the specified pattern (e.g., ".uninstall")
    async def plugin_uninstaller(event):
        # Create an instance of PluginManager
        plugin = PluginManager()

        # Call the uninstall_plugin method to handle plugin uninstallation
        await plugin.uninstall_plugin(event)