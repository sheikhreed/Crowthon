# Import sleep to add delay between operations
from asyncio import sleep

# Import Reboot function to restart the bot after plugin changes
from misc import Reboot

# Import necessary OS-level function
from os import remove

# Define the plugin manager class with methods to install and uninstall plugins
class PluginManager:
    # Asynchronous method to install a plugin
    async def install_plugin(self, event):
        # Notify the user that the installation process has started
        await event.edit("The plugin installation process has been activated.")
        try:
            # Wait for 2 seconds before proceeding
            await sleep(2)

            # Check if the command was used in reply to a message
            if event.reply_to:
                # Fetch the replied message
                self.get_plugin = await event.get_reply_message()

                # Check if the replied message contains media (a file)
                if self.get_plugin.media:
                    # Extract the MIME type of the media file
                    self.mime_type = self.get_plugin.media.document.mime_type

                    # Check if the file is a Python script
                    if self.mime_type == "text/x-python":
                        # Download the plugin file into the plugins directory
                        await self.get_plugin.download_media(file="crowthon/plugins")

                        # Inform the user about successful installation and reboot
                        await event.edit("Great news! The plugin installation has been successfully completed. To ensure optimal performance, Crowthon is currently rebooting. The new features will be available for use shortly.")

                        # Call the Reboot function
                        Reboot()
                    else:
                        # Inform the user if the file is not a Python file
                        await event.edit("The file you are trying to install as a plugin is not a Python file. Please use a valid plugin file.")
                else:
                    # Inform the user that no media file was provided
                    await event.edit("You are not trying to install any plugin file (media). Please attempt to install a valid plugin file.")
            else:
                # Inform the user that the command was not used as a reply
                await event.edit("You did not use the command in reply to a plugin file. Please try using the command in reply to the correct plugin file.")

        # Silently ignore any exceptions
        except:
            pass

    # Asynchronous method to uninstall a plugin
    async def uninstall_plugin(self, event):
        # Notify the user that the uninstallation process has started
        await event.edit("The plugin uninstallation process has been activated.")
        try:
            # Wait for 2 seconds before proceeding
            await sleep(2)

            # Check if the command was used in reply to a message
            if event.reply_to:
                # Fetch the replied message
                self.get_plugin = await event.get_reply_message()

                # Check if the replied message contains media (a file)
                if self.get_plugin.media:
                    # Extract the MIME type of the media file
                    self.mime_type = self.get_plugin.media.document.mime_type

                    # Check if the file is a Python script
                    if self.mime_type == "text/x-python":
                        # Get the file name of the plugin to remove
                        self.file_name = self.get_plugin.media.document.attributes[0].file_name

                        # Delete the plugin file from the plugins directory
                        remove(f"crowthon/plugins/{self.file_name}")

                        # Notify the user about successful uninstallation and reboot
                        await event.edit(f"The {self.file_name} plugin has been successfully uninstalled. Rebooting Crowthon to ensure a clean unload. Please wait a few moments for the process to complete.")

                        # Call the Reboot function
                        Reboot()
                    else:
                        # Inform the user if the file is not a Python file
                        await event.edit("The file you are trying to uninstall as a plugin is not a Python file. Please use a valid plugin file.")
                else:
                    # Inform the user that no media file was provided
                    await event.edit("You are not attempting to uninstall any plugin file (media). Please try to uninstall a valid plugin file.")
            else:
                # Inform the user that the command was not used as a reply
                await event.edit("You did not use the command in reply to a plugin file. Please try using the command in reply to the correct plugin file.")
        
        # Silently ignore any exceptions
        except:
            pass