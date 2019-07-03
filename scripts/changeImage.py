# coding:utf-8
import os
import glob
from PIL import Image
file_list = glob.glob('/media/baymin/c731be01-5353-4600-8df0-b766fc1f9b80/new-work/素材/yunsheng_date/韵升pascal voc/VOCdevkit/VOC2012/JPEGImages/*.bmp')
# bmp 转换为jpg
def bmpToJpg():
    for num, fileName in enumerate(file_list):
        # print(fileName)
        newFileName = fileName[0:fileName.find(".")]+".jpg"
        print(newFileName)
        im = Image.open(fileName)
        im.save(newFileName)

if __name__ == '__main__':
    bmpToJpg()
