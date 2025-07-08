#create tuple (Ready Only List)
tuple = ('Audi',100,3.14,True,False,'Audi')
print(tuple)
#tuple[0] = 'BMW' #here we trying change value in tuple
print('Good bye')
print(tuple[0]) #Audi
print(tuple[0:3]) # Audi 100 3.14
print('position of 100 in tuple',tuple.index(100)+1)
output =  'count of audi = ' + str(tuple.count('Audi'))
print(output)