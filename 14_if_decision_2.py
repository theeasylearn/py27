'''
    write a program to accept 24 hours format time from user and convert it into 12 hours format time and display it 
    time : 23 output 11:00 PM 
    time : 09 output 09:00 AM 
'''
time = int(input("Enter hours (between 1 to 24)"))
if time<0 or time>24:
    print("it is not valid time")
else:
    if time<13:
        print(f"{time}:00 AM ")
    if time>=13:
        time = time - 12 
        print(f"{time}:00 PM ")
print("Good Bye.")