fruits = ['apple', 'banana', 'cherry', 'apple', 'grape', 'banana']
#at the end new item 
fruits.append('graps')
#at the begining 
fruits.insert(0,'coconut')
print(fruits)
print('1st apple position',fruits.index('apple'))
print('total apple ',fruits.count('apple'))

basket = ['potato','onion']
basket.extend(fruits)
print(basket)

basket.remove('onion')
print(basket)
basket.pop(1)
print(basket)
basket.clear()
print(basket)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

#python never copy list, tuples, dictionary, set into another variable when we use = operator actually it store reference into variable
# fruits2 = fruits wrong way to copy list, tuples, dictionary, set
fruits2 = fruits.copy() 
fruits2.remove('cherry')
print(fruits)
print(fruits2)
