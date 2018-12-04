# coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "Annotations"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        # print(xmlFile, str(xmlFile))
        newname = str(xmlFile).replace('.xml', '.jpg')
        # print(newname)

        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 最核心的部分,路径拼接,输入的是具体路径
        root = dom.documentElement

        folder = root.getElementsByTagName('folder')  # 获取标签的值
        folder0 = folder[0]                           # 一个标签可能有多个值，这里只有一个
        folder0.firstChild.data = 'JPEGImages'        # 修改标签值

        filename = root.getElementsByTagName('filename')
        fliename0 = filename[0]
        fliename0.firstChild.data = newname

        """
        # 原始信息
        print("原始信息")
        print(folder0.firstChild.data)
        print(fliename0.firstChild.data)
        # 打印输出
        print("修改后的 folder:")
        print(folder0.firstChild.data)

        print("修改后的 filename:")
        print(fliename0.firstChild.data)
        print("*******")
        """
        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            # print('写入完成!')
