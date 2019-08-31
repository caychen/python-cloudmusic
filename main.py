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
from playlist.Playlist import __get_playlist, __remove_duplicate_song, __each_remove_duplicate_song

"参考：https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py"

Menus = ['关注人列表', '获取歌单', '排除未整理的重复歌曲', '相互排除未整理的重复歌曲', '退出']


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
                    5: __logout,
                }[index](response)
            print()

        except (KeyError, InterruptedError):
            print('输入错误...')
        except Exception as reason:
            print('main方法捕获异常：', reason)
