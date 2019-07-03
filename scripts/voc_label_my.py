import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('2012', 'big_yahen'), ('2012', 'dian'), ('2012', 'normal_yahen'), ('2012', 'others'), ('2012', 'xian')]

classes = ["big_yahen", "dian", "normal_yahen", "others", "xian"]


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    print('%s'%(image_id))
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('VOCdevkit/VOC%s/labels/%s.txt'%(year, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

if __name__ == '__main__':
    wd = getcwd()

    for year, image_set in sets:
        if not os.path.exists('VOCdevkit/VOC%s/labels/'%(year)):
            os.makedirs('VOCdevkit/VOC%s/labels/'%(year))
        image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
        list_file = open('%s_%s.txt'%(year, image_set), 'w')
        for image_id in image_ids:
            filename = os.path.splitext(image_id)[0]
            if filename == '1' or filename == '-1':
                continue
            list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, filename))
            convert_annotation(year, filename)
        list_file.close()

    os.system("cat *_*.txt > train.txt")
    os.system("cat *_*.txt > val.txt")

