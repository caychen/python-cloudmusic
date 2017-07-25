#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@file: phone_login.Login

@email: 412425870@qq.com

@author: Cay

@pythonVersion: Python3.5

@function: 

@version: 
'''
import json
import binascii
import os
import base64
from Crypto.Cipher import AES
import requests
import hashlib
from configparser import ConfigParser

session = None
csrf = None


"https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py"

default_timeout = 10

modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'

headers = {
        'Host':'music.163.com',
        #'Cookie' : 'appver=2.7.1;',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0'
    }
data = {}
limit = 20

# 登录加密算法, 基于https://github.com/stkevintan/nw_musicbox脚本实现
def encrypted_request(text):
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {'params': encText, 'encSecKey': encSecKey}
    return data

def createSecretKey(size):
    return ''.join([hex(x)[2:] for x in os.urandom(size)])[0:16]

def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode()

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1].encode()
    rs = int(binascii.hexlify(text), 16) ** int(pubKey, 16) % int(modulus, 16)
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
    return [each['nickname'] for each in _list if each['mutual'] == False]

  
if __name__ == '__main__':
    cf = ConfigParser()
    cf.read('account.ini', 'utf-8')
    user = dict(cf.items('account'))
    phone = user.get('phone')
    password = user.get('password')
    #print(phone, password)
    response = phone_login(phone, password)
    cookies = dict(response.cookies)
    global csrf
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
            if more == True:
                offset += limit
            else:
                break
            
        print(outOfFollows_nickname)
    else:
        print(response.get('msg'))
             
