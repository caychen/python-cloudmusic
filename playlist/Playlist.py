from common.Constant import csrf, get_session, headers, playlist_url, private_playlist_sheets, \
    public_playlist_sheets, public_playlist_code, private_playlist_code, playlist_detail_url, get_csrf, song_detail_url, \
    remove_song_url
from encrypt.Encrypt import encrypted_request
from entity.SongSheet import SongSheet


def __get_playlist(response):
    user_id = response['account']['id']
    offset = 0
    song_list = set()

    while True:
        # 请求参数
        text = {
            "offset": offset,
            "uid": user_id,
            "limit": 100,
            "csrf_token": get_csrf()
        }

        data = encrypted_request(text)
        try:
            response = get_session().post(playlist_url + get_csrf(), data=data, headers=headers)
            response.encoding = 'utf-8'
            r = response.json()

            playlist = r.get("playlist")

            for s in playlist:
                # 在显示的歌单中会包含收藏的歌单，去除掉，一般前面全是自己的歌单，后面的则是收藏歌单
                if s['userId'] == user_id:
                    song_sheet = SongSheet(s['id'], s['name'], s['privacy'])
                    song_list.add(song_sheet)

                    if s['privacy'] == private_playlist_code:
                        private_playlist_sheets.append(song_sheet)

                    if s['privacy'] == public_playlist_code:
                        public_playlist_sheets.append(song_sheet)

                else:
                    break

            if r.get("more"):
                offset += 100
            else:
                break

        except Exception as reason:
            print(reason)

    for song_sheet in song_list:
        print(song_sheet)
    print('')


public_song_ids = []
private_song_ids = []

private_exist_song_ids = []


def __get_list(playlist_sheets, privacy):
    req_text = {
        "id": '',
        "offset": 1000,
        "total": True,
        "limit": 1000,
        "n": 1000,
        "csrf_token": csrf
    }

    try:
        for playlist_sheet in playlist_sheets:
            req_text['id'] = playlist_sheet.id

            data = encrypted_request(req_text)

            response = get_session().post(playlist_detail_url + get_csrf(), data=data, headers=headers)
            response.encoding = 'UTF-8'
            r = response.json()

            track_ids = r.get('playlist').get('trackIds')
            if privacy == public_playlist_code:
                public_song_ids.extend(track_id.get('id') for track_id in track_ids)
            elif privacy == private_playlist_code:
                private_song_ids.extend(track_id.get('id') for track_id in track_ids)
    except Exception as reason:
        print('__get_list方法捕获异常：', reason)
        raise Exception


def __get_songs_detail(song_ids):
    req_text = {
        'ids': song_ids
    }
    data = encrypted_request(req_text)
    try:
        response = get_session().post(song_detail_url, data=data, headers=headers)
        response.encoding = 'UTF-8'
        r = response.json()
        return r
    except Exception as reason:
        print('__get_songs_detail方法捕获异常：', reason)
        raise Exception


def __remove_song(song_sheet_id, song_ids):
    req_text = {
        'pid': song_sheet_id,
        'trackIds': song_ids,
        'op': 'del'
    }

    data = encrypted_request(req_text)
    try:
        response = get_session().post(remove_song_url, data=data, headers=headers)
        response.encoding = 'utf-8'
        r = response.json()
        if r.get('code') == 200:
            return
        else:
            print()
    except Exception as reason:
        print('__remove_song方法捕获异常：', reason)
        raise Exception


def __remove_duplicate_song(response):
    try:
        if len(public_playlist_sheets) == 0:
            __get_playlist(response)

        # 获取所有已整理的歌曲id（只需执行一次）
        __get_list(public_playlist_sheets, public_playlist_code)

        # 遍历未整理的歌单id
        for private_playlist_sheet in private_playlist_sheets:
            # 获取指定私有歌单中的歌曲id
            __get_list([private_playlist_sheet], private_playlist_code)

            # 遍历私有歌单中的歌曲id
            for private_song_id in private_song_ids:
                if private_song_id in public_song_ids:
                    private_exist_song_ids.append(private_song_id)

            # 清除
            private_song_ids.clear()

            songs_detail = __get_songs_detail(private_exist_song_ids).get('songs')
            exist_song_names = []
            for song_detail in songs_detail:
                exist_song_names.append(song_detail.get('name'))

            if len(exist_song_names) != 0:
                print('私有歌单[' + private_playlist_sheet.name + ']有重复歌曲：[' + '，'.join(exist_song_names) + ']')
            else:
                print('私有歌单[' + private_playlist_sheet.name + ']无有重复歌曲')
            print('')

            # 进行删除
            if len(private_exist_song_ids) != 0:
                __remove_song(private_playlist_sheet.id, private_exist_song_ids)

            # 清空
            private_exist_song_ids.clear()

    except Exception as reason:
        print('__remove_duplicate_song方法捕获异常：', reason)
        raise Exception
