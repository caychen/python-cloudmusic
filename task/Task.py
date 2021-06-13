import json
import random

from common.Constant import headers, get_session, daily_sign_url, refresh_song_url, get_csrf, recommend_song_url, \
    feedback_song_url, playlist_detail_url
from encrypt.Encrypt import encrypted_request


def __daily_sign(response):
    req = {
        'type': 0
    }

    data = encrypted_request(req)
    res = get_session().post(url=daily_sign_url, data=data, headers=headers)
    ret = json.loads(res.text)

    if ret['code'] == 200:
        print("签到成功，经验+" + str(ret['point']))
    elif ret['code'] == -2:
        print("今天已经签到过了")
    else:
        print("签到失败 " + str(ret['code']) + "：" + ret['message'])


def __do_refresh_song_task(response):
    __csrf = get_csrf()


    req = {
        'csrf_token': __csrf
    }
    data = encrypted_request(req)
    res = get_session().post(url=recommend_song_url, data=data, headers=headers)
    ret = json.loads(res.text)
    if ret['code'] != 200:
        print("获取推荐歌曲失败 " + str(ret['code']) + "：" + ret['message'])
    else:
        lists = ret['recommend']
        music_lists = [(d['id']) for d in lists]

    music_id = []

    req = {
        'id': None,
        'n': 1000,
        'csrf_token': __csrf
    }

    # 歌单详情
    url = playlist_detail_url + __csrf
    for m in music_lists:
        req['id'] = m
        data = encrypted_request(req)
        res = get_session().post(url=url, data=data, headers=headers)
        ret = json.loads(res.text)

        for i in ret['playlist']['trackIds']:
            music_id.append(i['id'])

    # print("歌单大小：{musicCount}首\n".format(musicCount=len(music_id)))
    m = map(
        lambda x: {
            'action': 'play',
            'json': {
                'download': 0,
                'end': 'playend',
                'id': x,
                'sourceId': '',
                'time': 240,
                'type': 'song',
                'wifi': 0
            }
        },
        random.sample(music_id, 420 if len(music_id) > 420 else len(music_id)))

    req_text = {
        'logs': json.dumps(list(m))
    }

    data = encrypted_request(req_text)
    res = get_session().post(url=feedback_song_url, data=data)
    ret = json.loads(res.text)

    if ret['code'] == 200:
        print("刷听歌量成功")
    else:
        print("刷听歌量失败 " + str(ret['code']) + "：" + ret['message'])
