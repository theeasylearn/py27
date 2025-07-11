person = {'name':'Ankit Patel','age':41,'weight':81.25,'gender':True};

# we want to get all keys 
print(person.keys())

#we want to get only values
print(person.values())

#it is kind of list
keys = ['color','model','price','engineType']

#create dictionary using keys
car = dict.fromkeys(keys)
print(car)

#below line will generate error and code will stop 
# print(car['owner'])
print(car.get('owner','unknown'))
car['owner'] = "Ankit Patel"
print(car.get('owner','unknown'))
car.pop('price')
print(car)
#remove last key value pair
car.popitem()
print(car)