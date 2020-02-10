# -*- coding:utf8 -*-
import re

p = re.compile('------\n', re.S) # 已水平分割线为正则表达式

fileContent = open('Work/Book-All.md', 'r', encoding='utf8').read()  # 读文件内容到字符串

paraList = p.split(fileContent)  # 根据正侧表达式的匹配结果对文件进行切片

fileWriter = open('Work/List/Book-Part0.md', 'a', encoding='utf8')  # 创建一个写文件的句柄

for paraIndex in range(len(paraList)):  # 遍历切片后的文本列表
    fileWriter.write(paraList[paraIndex])  # 先将列表中第一个元素写入文件中
    fileWriter.close()  # 关闭当前句柄
    # 重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
    fileWriter = open('Work/List/Book-Part'+str(paraIndex+1) + '.md', 'a', encoding='utf8')

fileWriter.close()  # 关闭最后创建的那个写文件句柄

print('finished')
