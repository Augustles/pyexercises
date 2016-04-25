# coding=utf-8

import numpy as np  # 惯例

# Numpy数组是一个多维数组对象,
# 称为ndarray, 分为两个部分:
# 1. 实际的数据
# 2. 描述这些数据的元数据
a = np.array([0, 1, 2, 3, 4], dtype=int)  # 创建一个np单维数组
a.ndim  # 数组的维数(多维数组)
len(a)  # 单维返回元素个数
a.shape  # 数组的维度
a.size  # 数组元素总个数
a.dtype  # 数组中元素类型
a.itemsize  # 数组中每个元素字节大小
a.data


b = np.array([(1, 2, 3), (4, 5, 6)], dtype=float)  # 　创建二维数组
c = np.zeros((3, 5))  # 创建
b.ndim  #
len(b)  # 多维数组返回维数

a = np.arange(10)  # 创建一个单维数组
a[0], a[-1]
a[::-1], a[-2:]

b = np.arange(1, 10, 2)  # 和range相似
c = np.linspace(0, 1, 5)  # 起始点, 个数

a = np.ones((3, 3))  # 创建1,1,1,1数组
b = np.zeros((5, 5))  # 创建0,0,0数组
c = np.eye(3)  # 创建
d = np.diag(np.array([1, 2, 3, 4]))

a = np.random.rand(4)  # 创建[0,1]分布数组
b = np.random.randn(4)  # 高斯

# 数据类型int64, float64, int32, float32, complex128, S7
a = np.array([1 + 2j, 3 + 4j, 5 + 6 * 1j])
a.dtype  # dtype('complex128')
b = np.array([True, False, False, True])
b.dtype  # dtype('bool')
c = np.array(['Bonjour', 'Hello', 'Hallo', ])
c.dtype  # dtype('S7')最多包含7个字符
