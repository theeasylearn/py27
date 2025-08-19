#write a program to calculate & display simple interest of given amount,rate, year 
#next step 
# in case of run time error in program, program should recover from error and resume it's work (but how it is be done?)
while True: #this loop will run foreever 
    try:
        amount = int(input("Enter Amount"))
        rate = float(input("Enter Rate"))
        year = int(input("Enter year"))

        #calculate simple interest 
        interest = (amount * rate * year) / 100
        print(f"simple interest is = {interest}")
        break #stop loop after interest is display
    except ValueError:
        print("Invalid input (only numbers are allowed as input)")