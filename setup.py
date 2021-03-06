#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : DashenMQ_setup.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/6

import sys
import os
pypath = sys.executable
pypath = pypath.replace("pythonw","python")
print(pypath)


def pipsetup(packname):
    packcmd = "%s -m pip install %s" % (pypath, packname)
    print(packcmd)
    try:
        p = os.popen(packcmd)
    except UnicodeDecodeError:
        print("返回文本的格式编码有问题！")
    try:
        print(p.read())  # 执行cmd并得到返回的字符串
    except UnicodeDecodeError:
        print("读取返回值失败，大概意思是编码不对，不过已经执行完毕了")


if __name__ == '__main__':
    pipsetup("-r requirements.txt")
    print("安装完毕，现在可以通过support文件运行程序了！")

