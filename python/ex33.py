#coding:utf-8
q =input("please input a number")
numbers = []
i=0
while i<q:
    print "At the top i is %d" %i
    numbers.append(i)
    i+=1
    print "Numbers now: ",numbers
    print "At the bottom i is %d" %i

print "The numbers:"

for num in numbers:
    print num