# coding=utf-8

import os
# from collections import namedtuple
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent import monkey
monkey.patch_all()

# 验证码, 可以通过ajax接口验证
# 验证码不复杂，只使用了一种字体类型
# 验证码不复杂，只使用了一种字体大小
# 验证码不复杂，只使用了一种字体颜色
# 验证码不复杂，每张由5个字母或数字构成，5个字母或数字的位置都是固定的
# 验证码不复杂，没有图片的歪曲变形，没有干扰线条或图案
# 旋转, 扭曲
# 粘合一起

frm PIL import Image
from operator import itemgetter


im = Image.open('1460127832506.png')
# convert函数转换色彩模式
im.convert('1').show()  # 转为黑白单色图
im.convert('L').show()  # 转为灰度图(将黑白分为若干个等级)
im.convert('P')  # 保留全部信息


# 获取保留颜色(二值化)

im = Image.open('1460127832506.png')
im = im.convert('P')
his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

# 排名前十的色彩, pix依据这里值进行判断
for j, k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
    print j, k

im2 = Image.new('P', im.size, 255)
temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        temp[pix] = pix
        if pix == 220 or pix == 227:  # these are the numbers to get
            im2.putpixel((y, x), 0)

im2.save("output.png")


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
