#coding:utf-8
# *args 把所有的参数传入进来
def print_two(*args):
    arg1,arg2 =args
    print "arg1: %r,arg2 : %r" %(arg1,arg2)

def print_two_again(arg1,arg2):
    print "arg1: %r arg2: %r" %(arg1,arg2)

def print_one(arg1):
    print "arg1 %r" %(arg1)

def print_none():
    print "I got nothin'."

print_two("Xed","Shaw")
print_two_again("Zed","sdsad")
print_one("GDUSH")
print_none()
