# coding=utf-8

# sudo apt-get install tesseract-ocr
# pip install pytesseract
# pip install pillow
# 简单验证码
import pytesseract
import requests
from fabric.colors import green, red
import time
import os
try:
    import Image
except ImportError:
    from PIL import Image


def to_binary(img):
    # 图片二值化(黑白图片)
    image = Image.open(img)
    # 灰度化处理
    # 有很多种算法，这里选择rgb加权平均值算法
    gray_image = Image.new('L', image.size)
    # 获得rgb数据序列，每一个都是(r,g,b)三元组
    raw_data = image.getdata()
    gray_data = []
    for rgb in raw_data:
        value = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
        # value就是灰度值，这里使用127作为阀值，
        # 小于127的就认为是黑色也就是0 大于等于127的就是白色，也就是255
        if value < 127:
            gray_data.append(0)
        else:
            gray_data.append(255)
    gray_image.putdata(gray_data)
    gray_image.save(os.path.abspath(img)[:-4] + '.jpg')

    image.close()
    gray_image.close()

def get_code(file):
    img = Image.open(file)
    code = pytesseract.image_to_string(img)
    return code


def get_img(url):
    r = requests.get(url)
    fn = time.strftime('%Y-%m-%d-%H-%M-%S') + '-test.png'
    with open(fn, 'wb') as f:
        f.write(r.content)

url = 'http://test.51yyto.com/?/api/checkcode/image/80_27/1459993738615'

if not os.path.exists('captcha'):
    os.mkdir('captcha')

home = '/home/august/work/captcha'
os.chdir(home)
# for x in xrange(50):
#     get_img(url)
# print(red(get_code('genimage.png')))
for y in os.listdir(home):
    fn = os.path.abspath(y)
    if 'gen' in fn:
        # to_binary(fn)
        print(green(get_code(fn) + '==> ' + fn))



