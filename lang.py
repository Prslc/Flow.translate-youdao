from enum import StrEnum


class Lang(StrEnum):
    AUTO = "AUTO"
    EN = "EN"
    ZH_CHS = "ZH_CHS"
    ZH_CHT = "ZH_CHT"
    JA = "JA"
    KO = "KO"
    FR = "FR"
    DE = "DE"
    ES = "ES"
    RU = "RU"
    PT = "PT"
    IT = "IT"
    VI = "VI"
    TH = "TH"
    ID = "ID"
    AR = "AR"


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
