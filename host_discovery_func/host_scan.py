#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/2 16:36
# @Author     : yunkong
# @FileName   : host_scan.py
# @Description: 主机发现

import nmap


def scan_hosts(ip, mask):
    nm = nmap.PortScanner()
    nm.scan(hosts=f'{ip}/{mask}', arguments='-sn')
    alive_hosts = nm.all_hosts()
    for i in range(len(alive_hosts)):
        alive_hosts[i] += " is alive!!!"
    return alive_hosts


# if __name__ == '__main__':
#     print(scan_hosts('192.168.12.129', '28'))
