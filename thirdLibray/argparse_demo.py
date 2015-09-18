# encoding=utf-8

import argparse


# console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
T = '\033[93m'  # tan


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', help='show version')

    return parser.parse_args()
parse_args()


print(C + 'hello' + G + 'world' + R + '!')
