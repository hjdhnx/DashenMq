#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : 资源无损编码储存.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/6/2

import base64
from tkinter.filedialog import *
from tkinter.messagebox import *
from os import remove
from time import sleep
def get_filePath_fileName_fileExt(fileUrl):#获取文件上级目录,文件名称，文件后缀
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

def btn_savefiles(filecode=""):
    if filecode.startswith("filecode"):
        filetend = filecode.split('"')[0].split("@")[2].replace("=","").replace(" ","")
        filename = filecode.split('"')[0].split("@")[1]
        filecontent = filecode.split(" ")[2]
        savepath = asksaveasfilename(defaultextension=".%s" % filetend, filetypes=[("file", ".%s" % filetend)],initialfile="%s.%s" %(filename,filetend), title="选择路径并设置你要保存的文件名")
        if savepath!="":
            tmp = open(savepath, "wb+")
            content = base64.b64decode(filecontent)
            tmp.write(content)
            tmp.close()
            return savepath
    else:
        showerror("错误","没有传入可写的二进制文件数据！")

def btn_selectfile():
       fpath = askopenfilename()
       if fpath!="":
           _ ,fname,tp1=get_filePath_fileName_fileExt(fpath)
           form = tp1[1:]
           print(form)#打印文件类型
           open_file = open(fpath, "rb")
           b64str = base64.b64encode(open_file.read())
           open_file.close()
           sendfile = 'filecode@%s@%s = "%s"'%(fname,form,b64str)
           sendfile = sendfile.replace("b'","").replace("'","")
           f = open("file.txt", "w+")
           f.write(sendfile)
           f.close()
           return sendfile

def btn_delete(filepath,detime=1):#待删除的文件路径，延时删除秒数
    if filepath!="":
        sleep(detime)
        remove(filepath)

if __name__ == '__main__':
    file_code = btn_selectfile()
    print(file_code)
    a = btn_savefiles(file_code)
    # btn_delete(a,5)
