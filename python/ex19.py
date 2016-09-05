#codind:utf-8

def cheese_and_crackers(cheese_count,boxes_of_craclers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!"%boxes_of_craclers
    print "Man that's enough for a parry!"
    print "Get a blanket.\n"

print "We can just give the function number directly:"
cheese_and_crackers(20,30)

print "OR,We can ues variabnle from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do much inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can combine the two,variable and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)


a=raw_input()
b=input()
print a
print b

