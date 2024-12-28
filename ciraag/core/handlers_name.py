class CiraagPlugins:
    def __init__(self):
        self.default_plugins = [
            "ping_the_server"
        ]
        self.misc_plugins = [
            "get_self_destructive_media"
        ]
        self.helper_plugins = [
            "execute_helper",
            "set_helper"
        ]
        self.fighter_plugins = [
            "find_opponent",
            "remove_opponent",
            "chat_fighting",
            "slangs_bomb"
        ]

default_ciraag_plugins = CiraagPlugins().default_plugins
misc_ciraag_plugins = CiraagPlugins().misc_plugins
help_ciraag_plugins = CiraagPlugins().helper_plugins
fighter_ciraag_plugins = CiraagPlugins().fighter_plugins