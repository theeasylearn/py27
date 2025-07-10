# person = ['Ankit Patel',41,81.25,True];
#concept of dictionary {'key':value}
person = {'name':'Ankit Patel','age':41,'weight':81.25,'gender':True};
person['city'] = "Bhavnagar" #it will add new key value pair
person['name'] = "A. M. PATEL" #it will update exsiting key
print(person)
del person['city'] #it will delete city key and its value 
print(person)
print(person['age'])
print(person['weight'])
print(person['age'] * 365)