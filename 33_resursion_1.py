# write a program to convert decimal number into binary 
def toBinary(number):
    if number>0:
        reminder = number % 2
        number = number // 2
        toBinary(number) #recursion
        print(reminder,end=' ')
number = int(input("Enter number"))
toBinary(number)

