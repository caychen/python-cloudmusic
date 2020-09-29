import time

from common.Constant import headers, limit, profiles, csrf, get_session
from encrypt.Encrypt import encrypted_request


def __get_follows(user_id, offset):
    url = 'https://music.163.com/weapi/user/getfollows/{0}?csrf_token={1}'.format(user_id, csrf)
    headers['Referer'] = 'http://music.163.com/user/follows?id={0}'.format(user_id)
    req = {'offset': offset, 'limit': limit, 'csrf_token': csrf}
    response = get_session().post(url, data=encrypted_request(req), headers=headers)
    response.encoding = 'utf-8'
    return response.json()


def __parser(_list):
    return [(each['nickname'], profiles + str(each['userId'])) for each in _list if not each['mutual']]


def __get_none_follow(response):
    if 'account' in response:
        try:
            user_id = response['account']['id']
            none_follows_nickname = []
            offset = 0
            while True:
                response = __get_follows(user_id, offset)
                follows = response.get('follow')
                none_follows_nickname.extend(each for each in __parser(follows))
                more = response.get('more')
                if more:
                    offset += limit
                else:
                    break

                print("休息休息5s...")
                time.sleep(5000)

            print("不在关注列表中的：", none_follows_nickname)

        except Exception as reason:
            print(reason)
            return
    else:
        print(response.get('msg'))
