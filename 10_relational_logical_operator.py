#example of relational and logical operators 
#accept 3 input from user and use different type of relational and logical operators

num1 = int(input("Enter first number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

print(f"{num1} == {num2}",num1==num2)
print(f"{num1} != {num2}",num1!=num2)
print(f"{num1} < {num2}",num1<num2)
print(f"{num1} > {num2}",num1>num2)
print(f"{num1} <= {num2}",num1<=num2)
print(f"{num1} >= {num2}",num1>=num2)

print(f"{num1} == {num2} and {num2} == {num3}",num1==num2 and num2==num3)
print(f"{num1} == {num2} or {num2} == {num3}",num1==num2 or num2==num3)
print(f"not {num1} == {num2} and {num2} == {num3}",not(num1==num2 and num2==num3))