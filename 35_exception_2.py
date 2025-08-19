#concept of exception handling 
numbers = [10,20,30,40,'star',50,100,200,400,None]
# numbers = []
# numbers = ['ankit','viral','karan']
sum = 0 
count = 0 
for num in numbers:
    print(num)
    try:
        sum+=num
        count+=1
    except TypeError:
        print(f'got invalid input {num} so it is skipped')
try:
    average = sum / count
except  ZeroDivisionError:
    print("it seems list is empty or it has only invalid value")
else:
    print(f"sum = {sum} count = {count} average = {average}")