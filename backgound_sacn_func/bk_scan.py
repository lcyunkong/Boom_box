#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/3 11:56
# @Author     : yunkong
# @FileName   : bk_scan.py
# @Description:
import requests

from backgound_sacn_func.splic_url import *


def dir_scan(urls):
    results = []
    for url in urls:
        try:
            response = requests.get(url, timeout=2)
            results.append({f"{url}": f"{response.status_code}"})
        except requests.exceptions.RequestException:
            results.append({f"{url}": "访问错误，检查域名是否正确"})

    # print(results)
    return results


def dir_scan_start(host, list_file_name):
    list_url = get_spilc_url(host, list_file_name)
    return dir_scan(list_url)

# dir_scan_start("http://192.168.12.130:8080", ['php'])
