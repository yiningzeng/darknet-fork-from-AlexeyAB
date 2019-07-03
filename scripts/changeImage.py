# coding:utf-8
import os

from PIL import Image


# bmp 转换为jpg
def bmpToJpg(file_path):
    for fileName in os.listdir(file_path):
        # print(fileName)
        newFileName = fileName[0:fileName.find(".")]+".jpg"
        print(newFileName)
        im = Image.open(file_path+"/"+fileName)
        im.save(file_path+"/"+newFileName)

def main():
    file_path = "/media/baymin/c731be01-5353-4600-8df0-b766fc1f9b80/new-work/darknet/6-21-darknet/mupian/VOCdevkit/VOC2012/JPEGImages/"
    bmpToJpg(file_path)

if __name__ == '__main__':
    main()
