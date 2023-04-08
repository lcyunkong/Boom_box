#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/3 12:11
# @Author     : yunkong
# @FileName   : splic_url.py
# @Description:
import os


def load_dir_file(dict_dir_path):
    # dict_dir_path = 'dict/'
    dict_dir_list = []
    for filename in os.listdir(dict_dir_path):
        if os.path.isfile(os.path.join(dict_dir_path, filename)):
            dict_dir_list.append(filename)
    return dict_dir_list


def load_dict(dict_file):
    with open(dict_file, "r", encoding="UTF-8") as fp:
        return fp.readlines()


def spilc_url(host, uri_list):
    host = (host + "/").replace("//", "/").strip()
    # print(host)
    url_list = []
    for uri in uri_list:
        url_list.append((host + uri).replace("//", "/").replace(":/", "://").strip())
    return url_list


def get_spilc_url(host, file_name_list):
    url_list = []
    for file_name in file_name_list:
        uri_list = load_dict(f'../pubilc_resource/dict/{file_name}.txt')
        for url in spilc_url(host, uri_list):
            url_list.append(url)
    return url_list


# if __name__ == '__main__':
#     host = "http://192.168.12.130:8080/"
#     file_name = ["php", "dir"]
#     print(get_spilc_url(host, file_name))
