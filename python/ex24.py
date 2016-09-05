#coding:utf-8

print "Let's practice everything."
print 'You\'d need to know \'bout escapes witg\\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic firmly planted
cannot discern \n the needs of love
 nor comprehend passion from intution
 and requires an explanation
 \n\t\t where there is none.
"""
print "-"*15
print poem
print "-"*15

five = 10-2+3-6
print "This should be five: %s" %five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans /1000
    crates = jars /100
    return jelly_beans,jars,crates

start_point = 10000
#函数的几个返回值可以同时返回给几个变量
beams,jars,crates = secret_formula(start_point)

print "With a starting point of :%d" %start_point
print "We'd have %d beans,%d jars,and %d crates."%(beams,jars,crates)

start_point = start_point/10

print "We can also do that this way:"
#格式化输出的参数可以是函数的返回值
print "we'd have %d beans ,%d jars ,and %d crates ."%secret_formula(start_point)
