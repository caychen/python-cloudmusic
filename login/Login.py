import hashlib
# pip install request
from configparser import ConfigParser

import requests

from common.Constant import headers, set_session, set_csrf, phone_login_url
from encrypt.Encrypt import encrypted_request


def read_ini(ini_file_name, item):
    cf = ConfigParser()
    cf.read(ini_file_name, 'utf-8')
    return dict(cf.items(item))


def phone_login():
    user = read_ini('account.ini', 'account')
    phone = user.get('phone')
    password = user.get('password')
    # print(phone, password)

    text = {
        'phone': phone,
        'password': hashlib.md5(password.encode()).hexdigest(),
        'rememberLogin': 'true',
        'countrycode': '86'
    }

    data = encrypted_request(text)

    # 设置session
    session = requests.session()
    set_session(session)
    response = session.post(phone_login_url, headers=headers, data=data)
    response.encoding = 'utf-8'

    # 获取cookie和csrf并设置
    cookies = dict(response.cookies)
    csrf = cookies.get('__csrf')
    if csrf is None:
        print(response.text)
        # res = json.loads(response.text)
        exit(-1)

    set_csrf(csrf)

    _h = headers['Cookie']
    for (k, v) in cookies.items():
        _h = _h + " " + k + "=" + v + ";"

    headers['Cookie'] = _h
    print('登录成功')

    return response
