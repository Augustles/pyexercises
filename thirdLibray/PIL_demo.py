# coding=utf-8

import os
# from collections import namedtuple
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent import monkey
monkey.patch_all()

# 比较图片文件相似度


def similarity(f1, path=r'.'):
    from PIL import Image
    import math
    import operator
    os.chdir(path)
    files = [file for file in os.listdir(path)]
    image1 = Image.open(f1)
    for f2 in files:
        image2 = Image.open(f2)

        h1 = image1.histogram()
        h2 = image2.histogram()

        rms = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        # return rms
        if rms < 1000 and f1.split('\\')[-1] != f2:  # 100%相似结果为0, 数字越大相差大
            print rms, f1.split('\\')[-1], f2


try:
    similarity(file1)
except Exception, e:
    print(e)
    # with open('error.log','a') as f:
    #     import time
    #     f.wrte(time.strftime('%Y-%m-%d %H:%M:%S')+' => '+e)
    pass

# 压缩图片


def resize_img(img):
    from PIL import Image
    image = Image.open(img)
    w, h = image.size
    image.resize((w / 2, h / 2)).save('b.jpg')
