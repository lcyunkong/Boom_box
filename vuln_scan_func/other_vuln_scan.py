#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/6 20:47
# @Author     : yunkong
# @FileName   : other_vuln_scan.py
# @Description:
import os
import importlib
import pkgutil


def import_all_modules(dirname):
    for importer, module_name, _ in pkgutil.iter_modules([dirname]):
        full_module_name = '%s.%s' % (dirname, module_name)
        print(dirname, module_name)
        importer.find_module(module_name).load_module(full_module_name)


# print(import_all_modules("../pubilc_resource/poc_list/other/"))


from pubilc_resource.poc_list.other import CVE_2018_10933


def scan_vuln_py(hostname, port):
    res_list = []
    res = CVE_2018_10933.vuln_poc(hostname, port)
    res_list.append(res)
    return res_list


# print(scan_vuln_py('192.168.12.130', '2222'))
