#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/5 16:22
# @Author     : yunkong
# @FileName   : finger_main.py
# @Description:

from Wappalyzer import Wappalyzer, WebPage


def finger_scan(url):
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        res_dict = wappalyzer.analyze_with_versions_and_categories(webpage)
        res_list = []
        for index, value in res_dict.items():
            res_list.append(f"{index}: {res_dict[index]['versions']}")
        return res_list
    except:
        pass
    # print(wappalyzer.analyze(webpage))
    # print(wappalyzer.analyze_with_categories(webpage))
    # print(wappalyzer.analyze_with_versions_and_categories(webpage))
# finger_scan("http://192.168.12.129")