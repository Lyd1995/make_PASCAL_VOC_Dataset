# coding=utf-8
import os
import os.path
import shutil
from xml.etree.ElementTree import ElementTree, Element

path = "VOCtrainval2012/VOCdevkit/VOC2012/Annotations"
path_pic = "VOCtrainval2012/VOCdevkit/VOC2012/JPEGImages"
path_xml_dir = "VOC2012/Annotations"
path_pic_dir = "VOC2012/JPEGImages"
files = os.listdir(path)  # 得到文件夹下所有文件名称

for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        tree = ElementTree()
        tree.parse(os.path.join(path, xmlFile))
        tree_root = tree.getroot()
        xmlname = xmlFile.split(".")[0]
        picname = xmlname+".jpg"
        # print(picname)
        # print(type(picname))

        for i in range(2, (len(tree_root)-3)):
            object_name = tree_root[i][0].text
            if object_name == 'car' or object_name == 'bus':
                # print(object_name)
                picpath = os.path.join(path_pic, picname)
                shutil.copy(picpath, path_pic_dir)
                # 将这个文件复制到指定的文件夹
                tree.write(os.path.join(path_xml_dir, xmlFile), encoding='utf-8', xml_declaration=True)
                break