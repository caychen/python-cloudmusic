default_timeout = 10

MODULUS = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
NONCE = b'0CoJUm6Qyw8W8jud'
PUBKEY = '010001'

# 获取关注的每页数量
limit = 20

# 个人主页
profiles = 'https://music.163.com/#/user/home?id='
# 手机号登录请求的url
phone_login_url = 'https://music.163.com/weapi/login/cellphone'

# 请求头
headers = {
    'Host': 'music.163.com',
    # 'Cookie' : 'appver=2.7.1;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0'
}

session = None
csrf = None


def set_session(s):
    global session
    session = s


def get_session():
    return session


def set_csrf(c):
    global csrf
    csrf = c


def get_csrf():
    return csrf
