def getResult(num1,num2):
    add = num1 + num2 
    sub = num1 - num2 
    mul = num1 * num2 
    div = num1 / num2 
    return add,sub,mul,div 

num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))

result = getResult(num1,num2)
print(result)
print(result[0])
print(result[1])
print(result[2])
print(result[3])