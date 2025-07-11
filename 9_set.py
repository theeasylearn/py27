#create set
fruits = {'apple','kiwi','cherry'}
print(fruits)

fruits.add('mango')
fruits.add('mango') #ignored
fruits.add('mango') #ignored
print(fruits)

fruits.remove('kiwi')
print(fruits)

set1 = {1,2,3,4}
set2 = {5,2,3,6}
print(set1.union(set2)) #unique value 
print(set1.intersection(set2)) #common value
print(set1.difference(set2)) #all values which are in set1 but not in set2
print(set2.difference(set1)) #all values which are in set2 but not in set1