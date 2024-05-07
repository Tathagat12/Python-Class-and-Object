a = ["hey", "bro", "you'r ", "awesome"]

#iterating through a loop
for i in a:
    print(i)

# list having internaly __iter__ functions help to iterate list
print(dir(a))

#-------------------------------------------------list_iterator------------------------------------------------


itr = iter(a) # it return <list_iterator object at 0x000002126AC2ADA0>
print(itr)

# "for loop" work like this , internally it call next method
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))

#-------------------------------------------------list_reverseiterator------------------------------------------------

itr = reversed(a) # it return <<list_reverseiterator object at 0x000002126AC2ADA0>
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

