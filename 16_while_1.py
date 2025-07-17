'''
    write a program to findout whether given number is perfect number or not 

'''
num = int(input("Enter number")) #6
diviser = 1
sum = 0 
half = num // 2
while diviser<=half:
    reminder = num % diviser #0
    if reminder == 0:
        sum = sum + diviser # 1
    diviser = diviser + 1 #2 
    
if sum == num:
    print("it is perfect number")
else:
    print("it is not perfect number")