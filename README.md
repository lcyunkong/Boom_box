![logoko](https://s2.loli.net/2023/04/08/FJUDaG2L5pAbcgV.png)

## 关于 Boom_box

Boom_box使用了PyQT开发Windows界面，提供指纹识别、端口扫描、主机扫描、后台扫描等功能。



#### 使用方法

运行`interface/main_win.py`

![image-20230408120736535](https://s2.loli.net/2023/04/08/fwZpNvr9hs2KFco.png)

#### 指纹识别

![image-20230408121003698](https://s2.loli.net/2023/04/08/K64JDhUQfcMXybz.png)

#### 漏洞扫描

是根据public_resource/poc_list中的yaml文件进行扫描的，yaml文件可以自行定义，通过构造HTTP/HTTPS的数据包进行检测

![image-20230408121034683](https://s2.loli.net/2023/04/08/cNIHrSChoiKkFJX.png)

#### 其他扫描

可以扫描一些除HTTP/HTTPS协议才能利用的漏洞，是漏洞扫描模块的补充，运行python脚本进行检测

![image-20230408150837641](https://s2.loli.net/2023/04/08/eMpatYnScTsdOgH.png)

#### 主机探测

调用nmap模块进行检测，如果需要使用，需要先安装nmap并配置nmap的路径，详细自行百度

如果只输入目标NAT是端口扫描，子网掩码输入1-30可进行网段扫描

![image-20230408151822440](https://s2.loli.net/2023/04/08/ZDNslixkdTyrVS4.png)

#### 后台扫描

字典在public_resource/dict中，可以自行定义

![image-20230408151949551](https://s2.loli.net/2023/04/08/r5ukXxRsSl2YOyo.png)



## 联系我

#### 微信公众号

![微信公众号](https://s2.loli.net/2023/04/08/E5L7TdCtSPgpHsY.jpg)



