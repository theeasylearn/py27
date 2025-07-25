# write a program to print multiplication table of given number
number = int(input("enter number"))
for multiplier in range(1,11):
    answer = number * multiplier #5
    print(f"{number} X {multiplier} = {answer}")
    
