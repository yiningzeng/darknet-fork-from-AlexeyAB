# coding:utf-8
import glob
from PIL import Image
# /media/baymin/c731be01-5353-4600-8df0-b766fc1f9b80/new-work/素材/yunsheng_date/韵升pascal voc/VOCdevkit/VOC2012/JPEGImages/
xml_list = glob.glob('/media/baymin/c731be01-5353-4600-8df0-b766fc1f9b80/new-work/素材/yunsheng_date/另一半数据-郭-7-2/韵升引线框架-PascalVOC-export/Annotations/*.xml')

# bmp 转换为jpg
def append():
    for num, file in enumerate(xml_list):
        with open(file, 'a+') as f:
            f.write("annotation>")
            f.close()
        # with open(fileName, 'a+') as f:
        #     f.write("on>")

if __name__ == '__main__':
    append()
