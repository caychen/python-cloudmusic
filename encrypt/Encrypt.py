import base64
import binascii
import json
import os

# pip install pycryptodome
from Crypto.Cipher import AES

from common.Constant import NONCE, PUBKEY, MODULUS


def create_key(size):
    # return binascii.hexlify(os.urandom(size))[:16]
    return str(binascii.hexlify(os.urandom(size))[:16], encoding='utf-8')


# 请求加密算法, 基于https://github.com/stkevintan/nw_musicbox脚本实现
def encrypted_request(text):
    # type: (str) -> dict
    data = json.dumps(text)
    secret = create_key(16)
    params = aes(aes(data, NONCE), secret)
    encseckey = rsa(secret, PUBKEY, MODULUS)
    return {'params': params, 'encSecKey': encseckey}


def aes(text, key):
    # pad = 16 - len(text) % 16
    # text = text + bytearray([pad] * pad)
    # encryptor = AES.new(key, 2, b'0102030405060708')
    # ciphertext = encryptor.encrypt(text)
    # return base64.b64encode(ciphertext)

    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key.encode('utf8'), 2, b'0102030405060708')
    ciphertext = encryptor.encrypt(text.encode('utf8'))
    ciphertext = str(base64.b64encode(ciphertext), encoding='utf-8')
    return ciphertext


def rsa(text, pubkey, modulus):
    # text = text[::-1]
    # rs = pow(int(binascii.hexlify(text), 16),
    #          int(pubkey, 16), int(modulus, 16))
    # return format(rs, 'x').zfill(256)

    text = text[::-1]
    rs = int(text.encode('utf8').hex(), 16) ** int(pubkey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)
