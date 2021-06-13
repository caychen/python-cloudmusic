MODULUS = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
NONCE = '0CoJUm6Qyw8W8jud'
PUBKEY = '010001'

CHECK_TOKEN = '9ca17ae2e6ffcda170e2e6eebac17a8ebff8d0dc5bbbe78bb2d45f968a8fabb547a295b8d9f662bbabfeacbc2af0feaec3b92ae98c8e99b17fe9f086d1e75b939f8bb6d14f8eea8687ca6686908e90c6728ceaee9e'

# 获取关注的每页数量
limit = 20

# 个人主页
profiles = 'https://music.163.com/#/user/home?id='
# 手机号登录请求的url
phone_login_url = 'https://music.163.com/weapi/login/cellphone'
# 个人歌单url
personal_playlist_url = 'https://music.163.com/weapi/user/playlist?csrf_token='
# 歌单详情url
playlist_detail_url = 'https://music.163.com/weapi/v6/playlist/detail?csrf_token='
# 歌曲详情url
song_detail_url = 'http://music.163.com/weapi/song/detail?csrf_token='
# 删除/添加歌曲到歌单中的url
add_and_remove_song_url_from_sheet = 'https://music.163.com/weapi/playlist/manipulate/tracks?csrf_token='
# 退出网易云的url
logout_url = 'https://music.163.com/weapi/logout?csrf_token='
# 获取歌曲URL
playsheet_detail_url = "http://music.163.com/weapi/song/enhance/player/url?csrf_token="

# 每日签到url
daily_sign_url = "https://music.163.com/weapi/point/dailyTask"

# 刷歌url
refresh_song_url = "https://music.163.com/weapi/v6/playlist/detail?csrf_token="

# 推荐歌曲
recommend_song_url = "https://music.163.com/weapi/v1/discovery/recommend/resource"

# 等级url
personal_level_url = "https://music.163.com/weapi/user/level?csrf_token="

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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Referer": "http://music.163.com/",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "os=pc; osver=Microsoft-Windows-10-Professional-build-10586-64bit; appver=2.0.3.131777; channel=netease;"
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
