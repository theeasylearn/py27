#example of map function 
numbers = [10,20,30,40,50]

square = map(lambda num: num*num ,numbers)
temp = list(square)
print(temp)

countries = ['India','Russia','China']

countries_lower = map(lambda item: str.lower(item),countries)
print(list(countries_lower))