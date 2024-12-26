from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.plugins.fighter.chat_fight import Opponent

@Ciraag(rf"\{handler}bomb")
async def slangs_bomb(event):
    await event.delete()
    abuser_genie = Opponent()
    await abuser_genie.spammer_genie(event)