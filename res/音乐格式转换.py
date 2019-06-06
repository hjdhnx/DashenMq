#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : 音乐格式转换.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/3

import sys
import os
pypath = sys.executable
print(pypath)


def pipsetup(packname):
    packcmd = "%s -m pip install %s" % (pypath, packname)
    try:
        p = os.popen(packcmd)
    except UnicodeDecodeError:
        print("返回文本的格式编码有问题！")
    try:
        print(p.read())  # 执行cmd并得到返回的字符串
    except UnicodeDecodeError:
        print("读取返回值失败，大概意思是编码不对，不过已经执行完毕了")


def starttool(mp3path, output, form="wav"):
    if os.path.exists("ffmpeg.exe") and os.path.exists(
            "ffplay.exe") and os.path.exists("ffprobe.exe"):
        try:
            from pydub import AudioSegment
        except BaseException:
            print("本地不存在音乐处理支持库，开始安装pydub...")
            pipsetup("pydub")
            from pydub import AudioSegment
        # AudioSegment.converter = r"D:\ffmpeg\bin\ffmpeg.exe"

        def trans_mp3_to_wav(filepath):
            if os.path.exists(mp3path):
                song = AudioSegment.from_mp3(filepath)
                print(song)
                song.export("res/%s" % output, format=form)
            else:
                print("目标文件不存在!")
        trans_mp3_to_wav(mp3path)
    else:
        csdn_url = "https://blog.csdn.net/qq_32394351/article/details/90748900"
        ext_mpeg = os.path.exists("ffmpeg.exe")
        ext_play = os.path.exists("ffplay.exe")
        ext_probe = os.path.exists("ffprobe.exe")
        print("请将ffmpeg.exe,ffplay.exe,ffprobe.exe程序放到本文件同目录后再执行！")
        print("不会操作请访问作者csdn教程查看：%s" % csdn_url)
        print(
            "文件检测:ffmpeg.exe:%s,ffplay.exe:%s,ffprobe.exe:%s" %
            (ext_mpeg, ext_play, ext_probe))


if __name__ == '__main__':
    # pipsetup("pydub")
    starttool(r"C:\Users\dashen\Desktop\1688.mp3", "musc.wav")
