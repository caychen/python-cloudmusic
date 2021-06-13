#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file: main.py
@email: 412425870@qq.com
@author: caychen
@pythonVersion: Python3.8
@function:
@version: v2.5-增加删除下架歌曲和试听歌曲
"""
import random

from common.Constant import set_unsafe_proxy_ip
from common.MyProxy import proxies_ips
from follow.Follow import __get_none_follow
from login.Login import phone_login
from login.LoginOrLogout import __logout
from playlist.Playlist import __get_playlist, \
    __remove_duplicate_song, \
    __each_remove_duplicate_song, \
    __remove_single_playsheet_down_trial_songs, \
    __foreach_remove_duplicate_song, \
    __get_single_song_detail, \
    __remove_down_trial_song_from_all_private, \
    __collect_song_to_self_by_keyword, \
    __collect_song_to_self_by_input
from task.Task import __daily_sign, __do_refresh_song_task

"参考：https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py"

Menus = ['获取歌单',
         '关注人列表',
         '排除未整理的重复歌曲',
         '相互排除未整理的重复歌曲',
         '循环删除未整理的重复歌曲（自动）',
         '获取歌曲信息',
         '删除某个歌单中的下架歌曲和试听歌曲（需要输入歌单）',
         '删除所有私有歌单中的下架歌曲和试听歌曲',
         '歌曲收藏（自动根据搜索词查询）(待实现)',
         '歌曲收藏（手动输入歌单号）（待实现）',
         '每日签到',
         '刷歌任务',
         '退出']


def show_menu():
    """
        Show the main menu for user to select the option.
    """
    print('*' * 6 + '菜单' + '*' * 6)
    for (index, menu) in enumerate(Menus):
        print(' ' * 3 + '(' + str(index + 1) + '): ' + menu + ' ' * 3)


if __name__ == '__main__':
    proxy_ip = random.choice(proxies_ips)
    print('本次使用的代理为: ' + proxy_ip)
    proxies = {
        # 'http': "http://" + proxy_ip,
        'https': "https://" + proxy_ip,
    }

    # set_unsafe_proxy_ip(proxies)

    #
    response = None

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
                    1: __get_playlist,  # __get_playlist
                    2: __get_none_follow,  # __get_none_follow,
                    3: __remove_duplicate_song,  # __remove_duplicate_song
                    4: __each_remove_duplicate_song,
                    5: __foreach_remove_duplicate_song,
                    6: __get_single_song_detail,
                    7: __remove_single_playsheet_down_trial_songs,
                    # https://github.com/darknessomi/musicbox/wiki/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E6%96%B0%E7%89%88WebAPI%E5%88%86%E6%9E%90%E3%80%82
                    8: __remove_down_trial_song_from_all_private,
                    9: __collect_song_to_self_by_keyword,
                    10: __collect_song_to_self_by_input,
                    11: __daily_sign,
                    12: __do_refresh_song_task,
                    13: __logout,
                }[index](response)
            print()

        except (KeyError, InterruptedError):
            print('输入错误...')
        except Exception as reason:
            print('main方法捕获异常：', reason)
