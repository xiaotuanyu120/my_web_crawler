#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import cookielib


def user_cookie(url, username, password):
    "使用username和password模拟登陆url，并将cookie储存在文件中"
    # 创建cookie文件对象
    cookie_filename = username + ".cookie"
    cookie = cookielib.MozillaCookieJar(cookie_filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)

    # 使用自定义的opener模拟登陆
    values = {"username":"CE001",
              "password":"admin123"}
            #   "Submit":"Login"}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = opener.open(request)

    # 储存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
    return cookie_filename
