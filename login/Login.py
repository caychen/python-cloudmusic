#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@file: phone_login.Login

@email: 412425870@qq.com

@author: Cay

@pythonVersion: Python3.7

@function:

@version:
'''
import json
import binascii
import os
import base64
# pip install pycryptodome
from Crypto.Cipher import AES
# pip install request
import requests
import hashlib
from configparser import ConfigParser

session = None
csrf = None

"https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py"

default_timeout = 10

MODULUS = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
NONCE = b'0CoJUm6Qyw8W8jud'
PUBKEY = '010001'

# 个人主页
profiles = 'https://music.163.com/#/user/home?id='

headers = {
    'Host': 'music.163.com',
    # 'Cookie' : 'appver=2.7.1;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0'
}

data = {}
limit = 20


def create_key(size):
    return binascii.hexlify(os.urandom(size))[:16]


# 登录加密算法, 基于https://github.com/stkevintan/nw_musicbox脚本实现
def encrypted_request(text):
    # type: (str) -> dict
    data = json.dumps(text).encode('utf-8')
    secret = create_key(16)
    params = aes(aes(data, NONCE), secret)
    encseckey = rsa(secret, PUBKEY, MODULUS)
    return {'params': params, 'encSecKey': encseckey}


def aes(text, key):
    pad = 16 - len(text) % 16
    text = text + bytearray([pad] * pad)
    encryptor = AES.new(key, 2, b'0102030405060708')
    ciphertext = encryptor.encrypt(text)
    return base64.b64encode(ciphertext)


def rsa(text, pubkey, modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16),
             int(pubkey, 16), int(modulus, 16))
    return format(rs, 'x').zfill(256)


def phone_login(phone, password):
    url = 'https://music.163.com/weapi/login/cellphone'

    text = {
        'phone': phone,
        'password': hashlib.md5(password.encode()).hexdigest(),
        'rememberLogin': 'true'
    }

    global data
    data = encrypted_request(text)

    global session
    session = requests.session()
    response = session.post(url, headers=headers, data=data)
    response.encoding = 'utf-8'

    return response


def getFollows(userId, offset):
    url = 'https://music.163.com/weapi/user/getfollows/{0}?csrf_token={1}'.format(userId, csrf)
    headers['Referer'] = 'http://music.163.com/user/follows?id={0}'.format(userId)
    req = {'offset': offset, 'limit': limit, 'csrf_token': csrf}
    response = session.post(url, data=encrypted_request(req), headers=headers)
    response.encoding = 'utf-8'
    return response.json()


def parser(_list):
    return [(each['nickname'], profiles + str(each['userId'])) for each in _list if not each['mutual']]


if __name__ == '__main__':
    cf = ConfigParser()
    cf.read('account.ini', 'utf-8')
    user = dict(cf.items('account'))
    phone = user.get('phone')
    password = user.get('password')
    # print(phone, password)
    response = phone_login(phone, password)
    cookies = dict(response.cookies)

    csrf = cookies.get('__csrf')

    response = response.json()
    if 'account' in response:
        userId = response['account']['id']
        outOfFollows_nickname = []
        offset = 0
        while True:
            response = getFollows(userId, offset)
            follows = response.get('follow')
            outOfFollows_nickname.extend(each for each in parser(follows))
            more = response.get('more')
            if more:
                offset += limit
            else:
                break

        print(outOfFollows_nickname)
    else:
        print(response.get('msg'))
