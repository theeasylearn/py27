#write a program to count no of items and total of items in integer list 
numbers = [57, 12, 89, 34, 76, 23, 45, 67, 38, 5, 92, 18, 61, 80, 29, 71, 54, 99]
count = 0
sum = 0
for item in numbers:
    print(item)
    count+=1
    sum+=item
print(f"count = {count} sum = {sum}")