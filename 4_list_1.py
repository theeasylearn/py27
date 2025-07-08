list = ['Apple',100,3.14,True,False,'Audi',None]
numbers = [10,20]

print(list)
print(numbers)

#display value at 0th position
print(list[0])

#print 1st 3 value 
print(list[0:3])

#print last two value 
print(list[5:])

newlist = list + numbers
print(newlist)

print(numbers * 5)

#we can update any value in list 
list[0] = 'IPhone 15 pro max'
print(list)

#we can delete value in list 
del list[6]
print(list)

#delete list itself
del numbers

print(numbers)
print('Good bye')