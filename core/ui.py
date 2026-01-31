from pyflowlauncher import Plugin, ResultResponse, send_results, Result
from pyflowlauncher.api import copy_to_clipboard

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

    result_text = query_translate(query, settings_instance.settings)

    if not result_text.strip():
        result_text = "Translation failed or returned empty result"

    return send_results([Result(
        Title=result_text,
        SubTitle="Press enter to copy",
        IcoPath="Images/app.png",
        JsonRPCAction=copy_to_clipboard(result_text) if result_text else None
    )])
