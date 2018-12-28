# Web控制继电器

[![build status](https://secure.travis-ci.org/maxcountryman/flask-login.png?branch=master)](https://travis-ci.org/#!/maxcountryman/flask-login)

用web控制多路继电器，技术:

- Flask
- RPI.GPIO

## 树莓派接线

将树莓派引脚连接继电器

- GPIO.18 :信道1
- GPIO.23 :信道2
- GPIO.24 :信道3
- GPIO.25 :信道4

![](https://img2018.cnblogs.com/blog/720033/201812/720033-20181228110154160-2144878468.png)


## 运行

### 1. 树莓派命令：
```
$ python3 app.py
```

### 2. 浏览器打开

地址：<http://192.168.0.104:5000/>

`192.168.0.104`换成自己树莓派IP

![](https://img2018.cnblogs.com/blog/720033/201812/720033-20181228110414104-1173783001.png)

### 3. 点击(打开)，(关闭) 控制继电器