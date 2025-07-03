# working with variables 
name = "Viral Mehta"
age = 35
gender = True 
weight = 85.25
print(name)
print(age)
print("weight",weight)
print("gender = ",gender)

age = "thirty five"
name = 100 
#we can use variable name into double quotation 
print(f"name = {name} age = {age}")
#delete variable
del name 
print(name) #here program stop becasue variable was deleted. in case of error code wont execute further
print("welcome")