# encoding=utf-8

import requests
from time import time
from gevent import monkey
monkey.patch_all()
from gevent.pool import Group
from fabric.colors import cyan, red
import pyperclip  # pip install pyperclip 跨平台剪贴板

# 判断网址可用
urls = ['http://guge.io',
        'http://www.hxgoogle.com',
        'http://www.gugesou.cn',
        'http://s.bt.gg',
        'https://www.guge163.com',
        'https://www.higuge.com',
        'http://www.google52.com',
        'http://guge.droider.cn',
        'http://www.gugeqq.com',
        'https://www.52guge.com',
        'http://g.kvm.la',
        'http://www.glcopy.com',
        'http://www.guge.link',
        'https://www.booo.so',
        'http://www.gufensoso.com',
        'http://www.g363.com',
        'http://ggss.cc',
        'http://g.yh.gs',
        'http://google.checkme.com.cn',
        'http://www.googleforchina.com',
        'https://goge.ml',
        'http://guge.droider.cn',
        'http://gg.cellmean.com',
        'http://g.eeload.com',
        'http://g.weme.so',
        'http://g.lijun.me']


def rate_testing(a):
    try:
        st = time()
        r = requests.get(a)
        if r.status_code == 200:
            end = time()
            t = (end - st) / 60
            print(cyan('=>Testing=>{0} spend: {1:.3}'.format(a, t)))
            # 写入到剪切板
            if pyperclip.paste() not in urls:
                pyperclip.copy(a)

        else:
            print(red('=>Oh God!=>{0} is bad'.format(a)))
    except Exception:
        pass
g = Group()
g.map_async(rate_testing, urls).get()
