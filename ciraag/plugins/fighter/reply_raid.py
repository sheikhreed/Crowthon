from ciraag.core.module_injector import *
from ciraag.core.decorator import Genie
from ciraag.core.custom_handler import handler
from ciraag.plugins.fighter.chat_fight import Opponent

@Ciraag(rf"\{handler}so")
async def find_opponent(event):
    await event.delete()
    ciraag_user = Opponent()
    await ciraag_user.set_opponent(event)

@Ciraag(rf"\{handler}ro")
async def remove_opponent(event):
    await event.delete()
    ciraag_user = Opponent()
    await ciraag_user.remove_opponent(event)

@Genie()
async def chat_fighting(event):
    try:
        ciraag_user = Opponent()
        await ciraag_user.fighter_genie(event)
    except:
        pass