#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file: main.py
@email: 412425870@qq.com
@author: caychen
@pythonVersion: Python3.7
@function:
@version: v2.2-注销退出功能
"""

from follow.Follow import __get_none_follow
from login.LoginOrLogout import phone_login, __logout
from playlist.Playlist import __get_playlist, __remove_duplicate_song, __each_remove_duplicate_song, \
    __get_playsheet_detail, __foreach_remove_duplicate_song, __get_single_song_detail

"参考：https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py"

Menus = ['关注人列表', '获取歌单', '排除未整理的重复歌曲', '相互排除未整理的重复歌曲', '循环删除未整理的重复歌曲（自动）', '删除下架歌曲', '获取歌曲信息', '退出']


def show_menu():
    """
        Show the main menu for user to select the option.
    """
    print('*' * 6 + '菜单' + '*' * 6)
    for (index, menu) in enumerate(Menus):
        print(' ' * 3 + '(' + str(index + 1) + '): ' + menu + ' ' * 3)


if __name__ == '__main__':
    # 手机号登录
    response = phone_login()
    response = response.json()

    while True:
        # 显示菜单
        show_menu()
        try:
            index = input('请输入序号: ').strip().lower()
            if index == '':
                raise KeyError

            index = int(index)
            if index == 0:
                # 退出
                exit(0)

            elif index in list(range(1, len(Menus) + 1)):
                {
                    1: __get_none_follow,  # __get_none_follow,
                    2: __get_playlist,  # __get_playlist
                    3: __remove_duplicate_song,  # __remove_duplicate_song
                    4: __each_remove_duplicate_song,
                    5: __foreach_remove_duplicate_song,
                    6: __get_playsheet_detail, # https://github.com/darknessomi/musicbox/wiki/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E6%96%B0%E7%89%88WebAPI%E5%88%86%E6%9E%90%E3%80%82
                    7: __get_single_song_detail,
                    8: __logout,
                }[index](response)
            print()

        except (KeyError, InterruptedError):
            print('输入错误...')
        except Exception as reason:
            print('main方法捕获异常：', reason)
