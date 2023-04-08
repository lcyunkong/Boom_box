#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/1 10:20
# @Author     : yunkong
# @FileName   : scan_vuln.py
# @Description: 利用requests库进行发包，判断响应是否存在漏洞
import json

import requests


# request_scan功能：
# 读取poc文件后进行发包，将响应的结果传给check_response函数
def request_scan(protocol, host, poc_yaml_conf):
    # proxy = {
    #     'http': '127.0.0.1:8080',
    #     'https': '127.0.0.1:8080'
    # }

    info_conf = poc_yaml_conf['Info']
    request_conf_dict = poc_yaml_conf['Request']
    response_conf = poc_yaml_conf['Response']
    response = ''
    for i in range(len(request_conf_dict)):
        try:
            request_conf = request_conf_dict[f"re{i}"]
            # 发送HTTP请求
            response = requests.request(
                url=f"{protocol}://{host}" + request_conf['path'],
                # proxies=proxy,
                method=request_conf['method'],
                headers=request_conf['headers'],
                data=str(request_conf['data']).replace('\\r\\n', '\n')
            )
        except:
            pass
    # 调用response_scan
    return check_response(response_conf, response, info_conf)


# check_response函数功能：
# 获取request_scan穿过来的响应数据进行判断漏洞验证是否成功
def check_response(response_conf, response, info_conf):
    if response != '' and response.status_code == response_conf['status_code']:
        if response_conf['text_char'] and response_conf['text_char'] in response.text:
            return info_conf['description'] + ": Vulnerability exists！！！"
    return info_conf['description'] + ": Vulnerability does not exist！！！"


