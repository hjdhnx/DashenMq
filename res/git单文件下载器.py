#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : git单文件下载器.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/5

import os
import requests
from contextlib import closing

def get_filePath_fileName_fileExt(fileUrl):  # 获取文件上级目录,文件名称，文件后缀
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

def download(url):
    filepath, shotname, extension = get_filePath_fileName_fileExt(url)
    filename = shotname+extension
    print(filepath, filename)
    if not os.path.exists(filename):
        print("当前目录不存在该文件，尝试下载此文件")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        with closing(requests.get(url, headers=headers, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            data_count = 0
            with open(filename, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    data_count = data_count + len(data)
                    now_jd = (data_count / content_size) * 100
                    print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, filename), end=" ")
    else:
        print("文件%s已存在，无需重复下载"%filename)



if __name__ == '__main__':
    # download('https://raw.githubusercontent.com/hjdhnx/soundhelper/master/ffmpeg.exe')
    # download('https://raw.githubusercontent.com/hjdhnx/soundhelper/master/ffplay.exe')
    # download('https://raw.githubusercontent.com/hjdhnx/soundhelper/master/ffprobe.exe')
    download('https://dl.softmgr.qq.com/original/Development/npp.7.7.Installer.exe')

