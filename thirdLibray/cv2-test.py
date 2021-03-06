# coding=utf-8

import cv2
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# 灰度化 (彩色转成灰度==>黑和白间还有很多级别的灰色)
im = Image.open('22.png')
im = im.convert('L')  # 转为灰度图
im1 = cv2.imread('22.jpg', cv2.IMREAD_GRAYSCALE)  # 转为灰度

# ImageEnhance
# new_img = origin_image.convert('RGB')
# enhancer = PIL.ImageEnhance.Color(new_img) #变黑白
# enhancer = enhancer.enhance(0)
# enhancer = PIL.ImageEnhance.Brightness(enhancer) #亮度降低，降噪
# enhancer = enhancer.enhance(3)
# enhancer = PIL.ImageEnhance.Contrast(enhancer) #高对比
# enhancer = enhancer.enhance(8)


# 1. 分量法
# 2. 最大值法
# 3. 平均值法
# 4. 加权平均法

# 二值化 (转成纯黑白)
# 直接设定阈值, 为什么是140呢？试出来的，或者参考直方图
im = im.point(lambda x: 255 if x > 140 else 0)  # 简单设定阈值
im = im.convert('1')  # 转为黑白
# 1. 普通二值化
# 2. 自适应二值化
im1 = cv2.adaptiveThreshold(
    im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 40)
im1 = cv2.resize(im1, (0, 0), fx=4, fy=4)  # 将图片放大4倍, 方便降噪和识别
# 噪点 1, 2结合使用
# 1. 8邻域降噪, 小的噪点
# 2. 连通域降噪, 大的噪点

im1 = cv2.medianBlur(im1, 9)  # 均值滤波(模糊降噪)
im = im.filter(ImageFilter.MedianFilter())  # 中值滤波过滤(中值去噪)
# 维纳滤波
# 干扰线
# 1. cv2.HoughLines 检测直线
# 2. 寻找连通线???, http://blog.csdn.net/problc/article/details/5579475
# flood fill(提取字符)
h, w = im1.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(im1, mask, (0, 0), 255)

# 腐蚀算法
# kernel = np.ones((2, 2), np.uint8)
# erosion = cv2.dilate(im1, kernel, iterations=1)

# 膨胀算法
# kernel = np.ones((2, 2), np.uint8)
# erosion = cv2.erode(im1, kernel, iterations=1)


# 补点
# kernel = np.ones((1, 1), np.uint8)
# cv2.morphologyEx(im1, cv2.MORPH_OPEN, kernel)

# 标准化
# 1. 旋转, cv2.warpAffine函数就是进行旋转操作
# 2. 归一化

# 分割
# 1. 投影法
# 2. 连通区域法
# 3. 滴水算法???, http://livezingy.com/csharp-code-of-the-drop-fall-algorithm/
# 机器学习knn算法
