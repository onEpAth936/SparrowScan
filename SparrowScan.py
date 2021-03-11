#!/usr/bin/python
# coding=UTF-8
'''
@Author: onEpAth936
@LastEdit: 2021-3-10 12:23:21
'''
import socket,os,time,sys,requests
from whois import whois
#域名反查ip
def ip_check(url):
    ip = socket.gethostbyname(url)
    print(ip)

#识别网站是否存在cdn
#调用系统（win与linux都有）nslookup命令，返回结果ip数判断
def cdn_check(url):
    cdn_data = os.popen('nslookup'+' '+url)
    cdn_datas = cdn_data.read()#声明到cdn_datas中
    x = cdn_datas.count('.')
    print(x)
    if x>10:
        print("cdn存在")
    else:
        print("cdn不存在")

#端口扫描
def ports_check(ip):
    ports = {80,8080,3128,8081,9098,1080,21,23,443,23,21,69,22,25,110,9080,9090,8080,3389,8081,1521,1158,2100,1434}
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for port in ports:
        result = server.connect_ex((ip,port))#这里最里面的括号是把一个目标看做整体
        if result == 0:
            print(str(port)+'|open')
        else:
            print(str(port)+'|close')

#第三方库whois获取主机信息
#whois查询
def whois_check(url):
    data = whois(url)
    print(data)

#子域名查询
def zym_check(url):
    urls = url.replace('www','')
    for zym_data in open('dict.txt'):
        zym_data = zym_data.replace('\n','')
        url = zym_data+urls
        try:
            r = requests.get('http://' + url)
#            print(r.status_code)
            if r.status_code == 200:
                urlip = socket.gethostbyname(url)
                print(urlip + '|' + url)
                time.sleep(0.1)
            else:
                print('正在尝试下一个...')
        except Exception as e:
            pass



if __name__ == '__main__':
    print('''  _____ ____    ____  ____   ____    ___   __    __
 / ___/|    \  /    ||    \ |    \  /   \ |  |__|  |
(   \_ |  o  )|  o  ||  D  )|  D  )|     ||  |  |  |
 \__  ||   _/ |     ||    / |    / |  O  ||  |  |  |
 /  \ ||  |   |  _  ||    \ |    \ |     ||  `  '  |
 \    ||  |   |  |  ||  .  \|  .  \|     | \      /
  \___||__|   |__|__||__|\_||__|\_| \___/   \_/\_/
                                                    
                                                    ''')
    check1 = sys.argv[1]
    if check1 == '-u':
        check2 = sys.argv[2]
        x = check2.count('.')
        if x>=2:
            check3 = sys.argv[3]
            if check3 == 'zym':
                zym_check(check2)
            elif check3 == 'whois':
                whois_check(check2)
            elif check3 == 'cdn':
                cdn_check(check2)
            elif check3 == 'fc':
                ip_check(check2)
            else:
                print('请指定要查询的功能:子域名用‘zym’ whois查询用‘whois’ cdn识别用‘cdn’ 域名反查用‘fc’ ')
        else:
            print('请输入正确域名，如：www.aa.com')

    elif check1 == '-i':
        check2 = sys.argv[2]
        x = check2.count('.')
        if x==3:
            check3 = sys.argv[3]
            if check3 == 'ports':
                ports_check(check2)
            else:
                print('请指定要查询的功能:端口扫描用‘ports’')
        else:
            print('请输入正确IP地址')

    else:
        print('请用指令-u或-p')