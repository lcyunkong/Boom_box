#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/2 16:37
# @Author     : yunkong
# @FileName   : port_scan.py
# @Description: 利用sacpy进行端口扫描
import nmap


# syn半连接扫描
def scapy_syn(ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=f'{ip}', arguments='-sS')
    open_ports = []
    for index, value in nm[f"{ip}"]["tcp"].items():
        if nm[f"{ip}"]["tcp"][index]['state'] == "open":
            open_ports.append(str(index) + ' is open!!!!')
    return open_ports


# if __name__ == '__main__':
#     d = "192.168.12.129"
#     print(scapy_syn(d))
