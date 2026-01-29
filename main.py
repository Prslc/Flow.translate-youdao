# -*- coding: utf-8 -*-

import sys

from pathlib import Path
from flowlauncher import FlowLauncher
from pyflowlauncher import Plugin
from api import query_translate

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

plugin = Plugin()

class Translate(FlowLauncher):

    def __init__(self):
        self.settings = plugin.settings or {}
        self.app_token = self.settings.get("app_token", "")
        self.app_secret = self.settings.get("app_secret", "")
        self.lang_from = self.settings.get("lang_from", "Auto")
        self.lang_to = self.settings.get("lang_to", "English")

        super().__init__() 

    def query(self, query):
        result = query_translate(query, self.settings)
        return [
            {
                "Title": result,
                "SubTitle": "Press enter to translate",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "copy_to_clipboard",
                    "parameters": [result]
                }
            }
        ]

if __name__ == "__main__":
    Translate()