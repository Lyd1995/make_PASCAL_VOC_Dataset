# coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "VOC2007_Det_datasets/Annotations"
files = os.listdir(path)  # 得到文件夹下所有文件名称
#s = []
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        #doc = xml.dom.minidom.Document()
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 最核心的部分,路径拼接,输入的是具体路径
        root = dom.documentElement

        y_left_top = root.getElementsByTagName('y_left_top')  # 获取标签的值
        y_left_top0 = y_left_top[0]                           # 一个标签可能有多个值，这里只有一个

        height = root.getElementsByTagName('height')
        height0 = height[0]

        y_left_top0.firstChild.data = int(y_left_top0.firstChild.data) + int(height0.firstChild.data)  # 修改标签值

        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            # print('写入完成!')
