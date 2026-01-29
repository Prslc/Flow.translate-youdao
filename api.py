import requests
import uuid
import time
from utlis import encrypt, truncate
from settings import LANG_MAP

YOUDAO_URL = 'https://openapi.youdao.com/api'

def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def query_translate(q, settings):
    data = {}
    data['from'] = LANG_MAP[settings.get("lang_from", "Auto")]
    data['to'] = LANG_MAP[settings.get("lang_to", "English")]
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = settings.get("app_token", "") + truncate(q) + salt + curtime + settings.get("app_secret", "")
    sign = encrypt(signStr)
    data['appKey'] = settings.get("app_token", "")
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    translations = response.json().get('translation', [])
    return translations[0].strip('"') if translations else ""
