#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : 录音.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/22

import pyaudio
import wave
import os
import base64
from playsound import playsound
from threading import Thread
from time import sleep
import time

def thread_it(func, *args):
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()
def get_filePath_fileName_fileExt(fileUrl):#获取文件上级目录,文件名称，文件后缀
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

def baseluyin(inputpath="res/luyin/output.wav",outputpath="res/luyin/luyinfilecode.txt"):
    if inputpath != "":
        _, fname, tp1 = get_filePath_fileName_fileExt(inputpath)
        form = tp1[1:]
        print(form)  # 打印文件类型
        open_file = open(inputpath, "rb")
        b64str = base64.b64encode(open_file.read())
        open_file.close()
        sendfile = f'luyincode@{fname}@{form} = "{b64str}"'
        sendfile = sendfile.replace("b'", "").replace("'", "")
        f = open(outputpath, "w+")
        f.write(sendfile)
        f.close()
        return sendfile
def playaudio(audio_file):
    global pyadplay
    pyadplay = pyaudio
    chunk = 1024  # 2014kb
    wf = wave.open(audio_file, 'rb')
    p = pyadplay.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)
    while True:
        data = wf.readframes(chunk)
        if len(data) == 0:
            break
        else:
            # print("dataplay",type(data))
            stream.write(data)
            pass
    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio
    print('wav音乐播放play函数结束！')
def luyin(path="res/luyin/output.wav",long=5.0):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = long # 设置录音的时间长度,单位秒
    WAVE_OUTPUT_FILENAME = path
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    print("* 录音开始")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    def end():
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("* 录音结束")
    # thread_it(end)
    end()
def saveRun(luyincode,savapath="res/luyin/saved.wav"):
    if not luyincode.startswith("luyincode"):
        pass
    else:
        filename = luyincode.split('"')[0].split("@")[1]
        filetend = luyincode.split('"')[0].split("@")[2].replace("=", "").replace(" ", "")
        # print(filetend)
        filecontent = luyincode.split(" ")[2]
        tmp = open(savapath, "wb+")
        tmp.write(base64.b64decode(filecontent))
        tmp.close()
        print(f"成功写入:{savapath}")
        def start_msg():
                absp = os.path.abspath(savapath)
                print(absp)
                playsound(savapath)  # 播放任意格式
                # os.remove(savapath)

        print("0.5秒后播放录音")
        # sleep(0.5)
        # start_msg()
        playaudio(savapath)
def moni():
    pass


if __name__ == '__main__':
    if not os.path.exists("res/luyin/"):
        os.mkdir("res/luyin/")
    while True:
        luyin(long=1)
        # id =time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        def now():
            id = "testluyin"
            a = baseluyin()
            print(a)
            saveRun(a,f"res/luyin/{id}.wav")


        thread_it(now)