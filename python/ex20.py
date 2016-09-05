#coding:utf-8

from sys import argv

script ,input_file = argv
# f 是一个变量名，这个变量代表一个文件
def print_all(f):
    print  f.read()

def rewind(f):
    f.seek(0)  #seek（0） 是回到文件的0 byte
#readline 是是读取一行，然后指向下一行
def print_a_line(line_count,f):
    print line_count,f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind,kind of like a tape."
#将文件重新回到文件的开始，好处是不用重新打开文件
rewind(current_file)

print "Let's print three lines:"



for current_line in range(1,4,1):
    print_a_line(current_line, current_file)



