from typing import TypedDict, Literal, cast
from pyflowlauncher import Plugin

from .lang import LANG_MAP

plugin = Plugin()

Settings = TypedDict(
    "Settings",
    {
        "app_token": str | None,
        "app_secret": str | None,
        "lang_from": Literal[
            "Auto",
            "English",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Japanese",
            "Korean",
            "French",
            "German",
            "Spanish",
            "Russian",
            "Portuguese",
            "Italian",
            "Vietnamese",
            "Thai",
            "Indonesian",
            "Arabic",
        ],
        "lang_to": Literal[
            "English",
            "Chinese (Simplified)",
            "Chinese (Traditional)",
            "Japanese",
            "Korean",
            "French",
            "German",
            "Spanish",
            "Russian",
            "Portuguese",
            "Italian",
            "Vietnamese",
            "Thai",
            "Indonesian",
            "Arabic",
        ],
    },
)


class TranslateSettings:
    def __init__(self):
        raw_settings = plugin.settings or {}
        self.raw_settings = raw_settings.copy()
        self.settings: Settings = cast(Settings, raw_settings.copy())

        self.app_token = self.settings.get("app_token", "")
        self.app_secret = self.settings.get("app_secret", "")

        self.settings["lang_from"] = LANG_MAP.get(
            self.settings.get("lang_from", "Auto"), "AUTO"
        )
        self.settings["lang_to"] = LANG_MAP.get(
            self.settings.get("lang_to", "English"), "EN"
        )
