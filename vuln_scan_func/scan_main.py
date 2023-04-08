#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/1 18:25
# @Author     : yunkong
# @FileName   : scan_main.py
# @Description:
from vuln_scan_func.load_yaml import *
from vuln_scan_func.scan_vuln import request_scan


def vuln_scan_start(protocol, host, server):
    res_vuln = []
    yaml_dir = f"../pubilc_resource/poc_list/{server}"

    # 读取yaml文件

    poc_list = load_yaml_dir(yaml_dir)
    for poc in poc_list:
        poc_yaml_conf = load_yaml(f"{yaml_dir}/{poc}", host)
        # 开始扫描漏洞
        res_vuln.append(request_scan(protocol, host, poc_yaml_conf))
    return res_vuln


# print(vuln_scan_start("http", "192.168.12.130:8000", "django"))
