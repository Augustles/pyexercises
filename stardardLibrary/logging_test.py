#!/usr/bin/env python
# encoding: utf-8

import os
import logging
from logging import Formatter, StreamHandler, FileHandler

# logging模块输出格式
fmt = Formatter('[%(asctime)s] %(levelname)s: %(message)s')
proxy = logging.getLogger('proxy')
# 输出到文件
fhd = logging.FileHandler('proxy.log')
fhd.setFormatter(fmt)
proxy.addHandler(fhd)
proxy.setLevel(logging.INFO)
# 输出到控制台
stdout_hd = logging.StreamHandler()
stdout_hd.setFormatter(fmt)
proxy.addHandler(stdout_hd)
proxy.setLevel(logging.INFO)
proxy.info('error')
