from enum import StrEnum


class Lang(StrEnum):
    AUTO = "auto"
    EN = "en"
    ZH_CHS = "zh-CHS"
    ZH_CHT = "zh-CHT"
    JA = "ja"
    KO = "ko"
    FR = "fr"
    DE = "de"
    ES = "es"
    RU = "ru"
    PT = "pt"
    IT = "it"
    VI = "vi"
    TH = "th"
    ID = "id"
    AR = "ar"


LANG_MAP = {
    "Auto": Lang.AUTO,
    "English": Lang.EN,
    "Chinese (Simplified)": Lang.ZH_CHS,
    "Chinese (Traditional)": Lang.ZH_CHT,
    "Japanese": Lang.JA,
    "Korean": Lang.KO,
    "French": Lang.FR,
    "German": Lang.DE,
    "Spanish": Lang.ES,
    "Russian": Lang.RU,
    "Portuguese": Lang.PT,
    "Italian": Lang.IT,
    "Vietnamese": Lang.VI,
    "Thai": Lang.TH,
    "Indonesian": Lang.ID,
    "Arabic": Lang.AR
}
