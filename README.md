## SparrowScan

一款多功能扫描器，项目刚开始，后续优化与完善。功能：域名反查，cdn识别，端口扫描，whois查询，子域名枚举



### 使用方法

命令格式：SparrowScan.py	参数	域名或IP 	功能

```
参数
-u	指定域名
-i	指定IP
```

```
功能
zym	子域名
whois	whois查询
cdn	识别cdn是否存在
fc	域名反查
ports	常见端口扫描
```



举例：子域名枚举

![1615440345389](E:\mypyproject\image\1615440345389.png)



### 常见问题

可能会提示whois模块不可用

解决方法：把项目中Lib\site-packages目录下的`whois`与`whois-0.7.3-py3.7.egg-info`文件夹，复制到你python环境的Lib\site-packages目录下



### 后续优化

- 多线程
- 功能优化
- 新增功能



### 有问题或是建议可以提issue