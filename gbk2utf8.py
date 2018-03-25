# encoding = utf-8
import os
import sys


def gbk2utf(path):
    with open(path, "r", encoding='gbk') as raw_file:
        content = raw_file.read()
        raw_file.close()
    with open(path, "w", encoding='utf-8') as out_file:
        out_file.write(content)
        out_file.close()


def ldir(path):
    print('开始转换'+path)
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        tdir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(tdir):  # 如果是文件夹则跳过
            ldir(tdir)
        else:
            gbk2utf(tdir)
    print("{}{}---------------------".format(path, '转换完成'))


if __name__ == '__main__':
    # TODO 添加命令行工具，目前需要在main中修改
    path = './hh'
    ldir(path)
