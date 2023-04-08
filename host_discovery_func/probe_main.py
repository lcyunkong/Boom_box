#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/1 16:37
# @Author     : yunkong
# @FileName   : probe_main.py
# @Description:
import ipaddress
import threading

from host_discovery_func.host_scan import *
from host_discovery_func.port_scan import *


def host_probe_start(host, mask):
    if mask == '':
        return scapy_syn(host)
    elif 0 < int(mask) <= 30:
        return scan_hosts(host, mask)


# print(host_probe_start('192.168.12.1', '30'))
