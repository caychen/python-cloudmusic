import time

from common.Constant import headers, limit, profiles, csrf, get_session, get_csrf, get_followed_list
from encrypt.Encrypt import encrypted_request


def __get_follows(user_id, offset):
    url = get_followed_list + get_csrf()
    req = {
        'offset': offset,
        'limit': limit,
        'csrf_token': get_csrf(),
        'userId': user_id,
        'total': "true"
    }
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
                follows = response.get('followeds')
                none_follows_nickname.extend(each for each in __parser(follows))
                more = response.get('more')
                if more:
                    offset += limit
                else:
                    break

                print("休息休息5s...")
                time.sleep(5)

            print("不在关注列表中的：", none_follows_nickname)

        except Exception as reason:
            print(reason)
            return
    else:
        print(response.get('msg'))
