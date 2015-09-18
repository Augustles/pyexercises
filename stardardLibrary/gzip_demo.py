# encoding=utf-8

import gzip
import zipfile
import os

# 压缩单个文件
with open('screenshot.bmp', 'rb') as f, gzip.open('screenshot.bmg.gz', 'wb') as w:
    w.writelines(f)

# 压缩文件夹


def zip_dir(path):
    files = [os.path.abspath(x)
             for x in os.listdir(path) if x.endswith('.png')]
    # print files
    zf = zipfile.ZipFile('test.gz', 'w', zipfile.ZIP_DEFLATED)
    print '=> compressing files...'
    for i in files:
        zf.write(i)
    zf.close()
    print '=> zf done...'
