num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))

print(f"num1 = {num1} num2 = {num2}",id(num1),id(num2))
result = num1 is num2 
result2 = num1 is not num2 
print(result,result2)
