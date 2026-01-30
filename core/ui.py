from pyflowlauncher import Plugin, ResultResponse, send_results, Result

from .api import query_translate
from .settings import TranslateSettings

plugin = Plugin()
settings_instance = TranslateSettings()


@plugin.on_method
def query(query: str) -> ResultResponse:
    if not settings_instance.app_token or not settings_instance.app_secret:
        return send_results([Result(
            Title="API credentials missing",
            SubTitle="Set your app_token and app_secret in plugin settings",
            IcoPath="Images/app.png"
        )])

    if not query.strip():
        return send_results([Result(
            Title="Please enter text to translate",
            SubTitle=f"{settings_instance.raw_settings.get('lang_from', 'Auto')} -> {settings_instance.raw_settings.get('lang_to', 'English')}",
            IcoPath="Images/app.png"
        )])

    result = query_translate(query, settings_instance.settings)
    return send_results([Result(
        Title=result,
        SubTitle="Press enter to copy",
        IcoPath="Images/app.png",
        JsonRPCAction={"method": "copy_to_clipboard", "parameters": [result]}
    )])
