# -*- coding: utf-8 -*-

import sys

from typing import cast
from pathlib import Path
from flowlauncher import FlowLauncher
from pyflowlauncher import Plugin

from api import query_translate
from lang import LANG_MAP
from settings import Settings

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

plugin = Plugin()


class Translate(FlowLauncher):

    def __init__(self):
        raw_settings = plugin.settings or {}
        self.raw_settings = raw_settings.copy()
        self.settings: Settings = cast(Settings, raw_settings.copy())

        self.app_token = self.settings.get("app_token", "")
        self.app_secret = self.settings.get("app_secret", "")

        self.settings["lang_from"] = LANG_MAP.get(
            self.settings.get("lang_from", "Auto"), "AUTO")
        self.settings["lang_to"] = LANG_MAP.get(
            self.settings.get("lang_to", "English"), "EN")

        super().__init__()

    def query(self, query):
        if not self.app_token or not self.app_secret:
            return [
                {
                    "Title": "API credentials missing",
                    "SubTitle": "Set your app_token and app_secret in plugin settings",
                    "IcoPath": "Images/app.png"
                }
            ]

        if not query.strip():
            return [
                {
                    "Title": "Please enter text to translate",
                    "SubTitle": f"{self.raw_settings.get('lang_from', 'Auto')} -> {self.raw_settings.get('lang_to', 'English')}",
                    "IcoPath": "Images/app.png"
                }
            ]

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
