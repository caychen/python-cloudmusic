import hashlib
# pip install request
import json
from configparser import ConfigParser

import requests

from common.Constant import headers, set_session, set_csrf, phone_login_url, get_csrf, get_session, personal_level_url
from encrypt.Encrypt import encrypted_request


def read_ini(ini_file_name, item):
    cf = ConfigParser()
    cf.read(ini_file_name, 'utf-8')
    return dict(cf.items(item))


def __get_level(loginData):
    url = personal_level_url + get_csrf()
    res = get_session().post(url=url, data=loginData, headers=headers)
    ret = json.loads(res.text)
    return ret["data"]


def phone_login():
    user = read_ini('account.ini', 'account')
    phone = user.get('phone')
    password = user.get('password')
    # print(phone, password)

    req_text = {
        'phone': phone,
        'password': hashlib.md5(password.encode()).hexdigest(),
        'rememberLogin': 'true',
        'countrycode': '86'
    }

    data = encrypted_request(req_text)

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
        # res = json.loads(response.req_text)
        exit(-1)

    set_csrf(csrf)

    _h = headers['Cookie']
    for (k, v) in cookies.items():
        _h = _h + " " + k + "=" + v + ";"

    headers['Cookie'] = _h

    ret = json.loads(response.text)
    # userid
    user_id = ret["profile"]["userId"]
    # 昵称
    nickname = ret["profile"]["nickname"]
    # 关注
    follows = ret['profile']['follows']
    # 粉丝
    followeds = ret['profile']['followeds']

    # 获取等级
    level_response = __get_level(data)

    print('【{nickname}】({userid})登录成功,关注了[{follows}]人,有粉丝[{followeds}]人,当前等级[{level}]级,距离升级还需听[{leftCount}]首歌.'
        .format(
        nickname=nickname,
        userid=user_id,
        follows=follows,
        followeds=followeds,
        level=level_response['level'],
        leftCount=level_response['nextPlayCount'] - level_response['nowPlayCount']))
    print()

    return response
