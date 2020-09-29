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
# 个人歌单url
playlist_url = 'https://music.163.com/weapi/user/playlist?csrf_token='
# 歌单详情url
playlist_detail_url = 'http://music.163.com/weapi/v3/playlist/detail?csrf_token='
# 歌曲详情url
song_detail_url = 'http://music.163.com/weapi/song/detail?csrf_token='
# 删除/添加歌曲到歌单中的url
add_and_remove_song_url_from_sheet = 'https://music.163.com/weapi/playlist/manipulate/tracks?csrf_token='
# 退出网易云的url
logout_url = 'https://music.163.com/weapi/logout?csrf_token='
# 获取歌曲URL
playsheet_detail_url = "http://music.163.com/weapi/song/enhance/player/url?csrf_token="

'''
歌曲搜索url, 如果加上type参数，则表示根据类型查询，其中：
type=1：单曲
type=10：专辑
type=100：歌手
type=1000：歌单
type=1002：用户
...
'''
search_songs_url = "http://music.163.com/weapi/cloudsearch/get/web?csrf_token="

# 请求头
headers = {
    'Host': 'music.163.com',
    # 'Cookie' : 'appver=2.7.1;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

public_playlist_code = 0
private_playlist_code = 10

session = None
csrf = None
unsafe_proxy_ip = None
safe_proxy_ip = None


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


def set_unsafe_proxy_ip(p):
    global unsafe_proxy_ip
    unsafe_proxy_ip = p


def get_unsafe_proxy_ip():
    return unsafe_proxy_ip


def set_safe_proxy_ip(p):
    global safe_proxy_ip
    safe_proxy_ip = p


def get_safe_proxy_ip():
    return safe_proxy_ip
