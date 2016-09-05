#coding:utf-8
#导入sys模块 使用argv 参数变量
from sys import  argv
#从参数变量中获取数据
script,filename = argv
#打开文件
txt = open(filename)
#打印文件内容
print "Here's your file %r:" %filename
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input(">>")

txt_again = open(file_again)
print txt_again.read()
txt.close()



