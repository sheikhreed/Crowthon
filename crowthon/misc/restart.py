# Import execvp to replace the current process with a new one
from os import execvp

# Define a Reboot class to handle restarting the Crowthon
class Reboot:
    def __init__(self):
        # Replace the current Python process with a new one running 'uv run crowthon'
        # This ensures the process is restarted cleanly without spawning a new process
        execvp("uv", ["uv", "run", "crowthon"])