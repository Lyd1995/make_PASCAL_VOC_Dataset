# coding=utf-8
import os
import os.path
from xml.etree.ElementTree import ElementTree, Element

path = "VOC2007_Det_datasets/Annotations"
files = os.listdir(path)  # 得到文件夹下所有文件名称

for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        tree = ElementTree()
        tree.parse(os.path.join(path, xmlFile))
        tree_root = tree.getroot()

        for i in range(3, len(tree_root)):
            bounding_box = tree_root[i][2]

            x_left_top = bounding_box[0].text
            y_left_top = bounding_box[1].text
            width = bounding_box[2].text
            height = bounding_box[3].text

            x_right_bottom_str = str(int(x_left_top) + int(width))
            y_right_bottom_str = str(int(y_left_top) + int(height))

            elementx = Element('x_right_bottom')
            elementy = Element('y_right_bottom')

            elementx.text = x_right_bottom_str
            elementy.text = y_right_bottom_str

            bounding_box.append(elementx)
            bounding_box.append(elementy)

            tree.write(os.path.join(path, xmlFile), encoding='utf-8', xml_declaration=True)
