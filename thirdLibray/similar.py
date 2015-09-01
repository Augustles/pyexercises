# coding=utf-8

import os
# from collections import namedtuple
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent import monkey
monkey.patch_all()

# 比较图片文件相似度


def similarity(f1, f2):
    from PIL import Image
    import math
    import operator

    image1 = Image.open(f1)
    image2 = Image.open(f2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    rms = math.sqrt(
        reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    # return rms
    if rms < 200:  # 100%相似结果为0, 数字越大相差大
        if f2 not in d.iterkeys() and f2 not in d.iterkeys():
            d[f1] = (f2, rms)
            print rms, f1, f2

base = r'C:\Users\ieware\Pictures'
os.chdir(base)
lists = [file for file in os.listdir(base)]
d = {}
for x in lists:
    for y in lists:
        if x != y and 'jpg' in x and 'jpg' in y:
            similarity(x, y)
