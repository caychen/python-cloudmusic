import hashlib
# pip install request
from configparser import ConfigParser

import requests

from common.Constant import headers, set_session, set_csrf, phone_login_url
from encrypt.Encrypt import encrypted_request


def __read_ini(ini_file_name, item):
    cf = ConfigParser()
    cf.read(ini_file_name, 'utf-8')
    return dict(cf.items(item))


def phone_login():
    user = __read_ini('account.ini', 'account')
    phone = user.get('phone')
    password = user.get('password')
    # print(phone, password)

    text = {
        'phone': phone,
        'password': hashlib.md5(password.encode()).hexdigest(),
        'rememberLogin': 'true'
    }

    data = encrypted_request(text)

    try:
        # 设置session
        session = requests.session()
        set_session(session)
        response = session.post(phone_login_url, headers=headers, data=data)
        response.encoding = 'utf-8'

        # 获取cookie和csrf并设置
        cookies = dict(response.cookies)
        csrf = cookies.get('__csrf')
        set_csrf(csrf)

    except Exception as reason:
        print(reason)
        exit(1)

    return response

def __logout():
    return