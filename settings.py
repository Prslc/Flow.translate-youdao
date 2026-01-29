import os
from typing import TypedDict, Literal

LANG_MAP = {
    "Auto": "AUTO",
    "English": "EN",
    "Chinese (Simplified)": "ZH_CHS",
    "Chinese (Traditional)": "ZH_CHT",
    "Japanese": "JA",
    "Korean": "KO",
    "French": "FR",
    "German": "DE",
    "Spanish": "ES",
    "Russian": "RU",
    "Portuguese": "PT",
    "Italian": "IT",
    "Vietnamese": "VI",
    "Thai": "TH",
    "Indonesian": "ID",
    "Arabic": "AR"
}

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
FLOW_PROGRAM_DIRECTORY = os.environ.get("FLOW_PROGRAM_DIRECTORY")
FLOW_APPLICATION_DIRECTORY = os.environ.get("FLOW_APPLICATION_DIRECTORY")

def is_portable():
    portable_data_path = os.path.join(FLOW_APPLICATION_DIRECTORY, "UserData")
    portable_data_deletion_indicator = os.path.join(FLOW_APPLICATION_DIRECTORY, "UserData", ".dead")
    return os.path.exists(portable_data_path) and not os.path.exists(portable_data_deletion_indicator)

if is_portable():
    DATA_DIR = os.path.join(FLOW_PROGRAM_DIRECTORY, "UserData")
else:
    DATA_DIR = os.path.expandvars("%APPDATA%\\FlowLauncher")

PLUGIN_SETTINGS_DIRECTORY = os.path.join(DATA_DIR, "Settings", "Plugins", "YoudaoTranslation") if FLOW_PROGRAM_DIRECTORY else None
SETTINGS_FILE = os.path.join(PLUGIN_SETTINGS_DIRECTORY, "Settings.json") if PLUGIN_SETTINGS_DIRECTORY else None