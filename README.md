<p align="center">
<a href="https://github.com/sheikhreed/Crowthon"><img src="assets/crowthon.png" height="128" width="128" alt="Crowthon"/></a>
</p>

<p align="center">
<b>Crowthon</b><br/>
<b>Crowthon</b> is a powerful Telegram Userbot written in <b>Python</b>, built on the <b>Telethon</b> library. It offers a rich set of automation tools tailored for both personal accounts and group management.
</p>

<p align="center">
<a href="https://www.python.org">
<img src="assets/python.svg" alt="Python"/></a>

<a href="https://github.com/LonamiWebs/Telethon">
<img src="assets/telethon.svg" alt="Telethon"/></a>
</p>

<p align="center">
<a href="https://render.com/deploy?repo=https://github.com/sheikhreed/Crowthon">
<img src="assets/deploy_to_render.svg" alt="Deploy to Render"/></a>
</p>

## Features
- Automation for Telegram accounts
- Group administration tools
- Dynamic **plugin system** for easy customization
- Secure and configurable
- Lightweight and suitable for low-resource devices

## Tech Stack
- Language: Python 3.10+
- Package Manager: uv
- Library: Telethon
- Database: MongoDB

## Deployment
Crowthon is ready for production deployment.
All setup instructions, required environment variables, and deployment steps are available in the official [**`Documentation`**](https://sheikhreed.github.io/Crowthon).

## Plugin System
Crowthon uses a plugin-based architecture. You can add new functionality by dropping Python files into the `plugins/` directory. Each plugin should follow a simple structure and can use Telethon events to handle messages, commands, or other interactions.

### Example Plugin
```python
from core import Crowthon, handler
from clients import crowthon

async def load_plugin(client):
    @Crowthon(pattern=rf"\{handler}hello")
    async def hello_world(event):
        await event.edit("Hello World")
```
You don’t need to manually register plugins – all Python files placed inside the `plugins/` directory are **automatically discovered and loaded** when Crowthon starts.

## Disclaimer
The purpose of this project is to improve the Telegram experience for users.
Crowthon does not provide or promote any features that violate Telegram’s Terms of Service.
> [!WARNING]
> If you use unofficial or third-party plugins, and they cause issues with your account, groups, channels, or privacy/security — the Crowthon project and its developers are not responsible for any consequences. Use at your own risk.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.