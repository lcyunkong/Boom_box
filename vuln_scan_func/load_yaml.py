#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time       : 2023/4/1 18:01
# @Author     : yunkong
# @FileName   : load_yaml.py
# @Description: 读取yaml文件
import yaml
import os


# 遍历目录中的所有yaml文件，并返回文件名的列表
def load_yaml_dir(yaml_dir):
    yaml_dir_list = []
    # 遍历目录中的所有文件
    for filename in os.listdir(yaml_dir):
        if os.path.isfile(os.path.join(yaml_dir, filename)):
            # 如果是文件，打印文件名
            yaml_dir_list.append(filename)
    return yaml_dir_list


# 读取yaml文件，并将host字段替换为目标ip
def load_yaml(yaml_file, host):
    # 读取配置文件
    with open(yaml_file, 'r', encoding='utf-8') as fp:
        yaml_conf = yaml.safe_load(fp)
    yaml_conf = yaml.dump(yaml_conf)
    yaml_conf = yaml_conf.replace('${Host}', host)
    yaml_conf = yaml.safe_load(yaml_conf)
    return yaml_conf

# if __name__ == '__main__':
    # print(load_yaml("poc_list/spring/CVE-2017-8046.yaml", "192.168.12.130:8080"))
    # print(load_yaml_dir("poc_list/spring"))
