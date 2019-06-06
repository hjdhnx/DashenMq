#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : 百度语音引擎.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/4

from aip import AipSpeech
import wave
import 音乐格式转换
file_object = None
aipSpeech = None


def default_init():
    APP_ID = '16427879'
    API_KEY = 'H1OOrfrsKCjZruv8SvWn3MHw'
    SECRET_KEY = 'we2ppcpEQi5Qj4lMvIZG1fCcMo6ztYaF '
    global aipSpeech
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    f = open("audiofile.txt", "w+")
    text = "《我们都是追梦人》 。\
                作曲 : 常石磊。\
                作词 : 王平久，编曲 : 柒玖、于昊。\
                每个身影 同阳光奔跑。 \
                我们挥洒汗水 回眸微笑。\
                一起努力 争做春天的骄傲。\
                懂得了梦想，越追越有味道。\
                我们都是追梦人，千山万水 奔向天地跑道。\
                你追我赶 风起云涌春潮，海阔天空 敞开温暖怀抱，我们都是追梦人，在今天 勇敢向未来报到。\
                当明天 幸福向我们问好，最美的风景是拥抱。\
                啦……啦……啦……。\
                每次奋斗 拼来了荣耀。\
                我们乘风破浪 举目高眺。"
    f.write(text)
    f.close()
    global file_object
    file_object = open('audiofile.txt')


def playaudio(audio_file):
    global pyadplay
    import pyaudio
    pyadplay = pyaudio
    chunk = 1024  # 2014kb
    wf = wave.open(audio_file, 'rb')
    p = pyadplay .PyAudio()
    stream = p.open(
        format=p.get_format_from_width(
            wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
    data = wf.readframes(chunk)  # 读取数据
    while True:
        data = wf.readframes(chunk)
        if len(data) == 0:
            break
        else:
            print(data)
            stream.write(data)
    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio
    print('wav音乐播放play函数结束！')


def start_t2a(spd=5, pit=5, vol=5, per=3):
    """

    :param spd: 合成语音的讲话速度
    :param pit: 合成语言的讲话音调
    :param vol: 合成语言的音量
    :param per: 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫,5为情感合成-小琪琪，默认为情感合成-度逍遥
    :return:
    """
    global file_object, aipSpeech
    try:
        n = file_object.read()
        print(n)
    finally:
        file_object.close()
    result = aipSpeech.synthesis(n, 'zh', 1, {'spd': spd, 'pit': pit,
                                              'vol': vol, 'per': per,
                                              })
    print(result)
    if not isinstance(result, dict):
        with open('res/txt2audio.mp3', 'wb') as f:
            f.write(result)
            音乐格式转换.starttool("res/txt2audio.mp3", "txt2audio.wav")


if __name__ == '__main__':
    default_init()  # 加载百度语言应用 默认用的本人的，做商用请找到这个函数，在里面改成你们自己的。里面加载了一个测试用的文本
    start_t2a(per=5)  # 开始文字转语音最终生成wav文件
    playaudio("res/txt2audio.wav")  # 播放
