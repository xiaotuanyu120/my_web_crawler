#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import cookielib

from login import user_cookie


def crawler_request(url, cookie_filename):
    "获取文件储存的cookie，并用其访问目标url"
    cookie = cookielib.MozillaCookieJar()
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
    request = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(request)
    return response


if __name__ == "__main__":
    # 获取用户的cookie
    login_url = "https://www.testdomain.com/login.php"
    username = "yourusername"
    password = "yourpassword"
    cookie_filename = user_cookie(login_url, username, password)

    # 使用cookie来发起请求
    url = "https://www.testdomain.com/main.php"
    response = crawler_request(url, cookie_filename)
    print response.read()
