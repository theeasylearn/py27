'''
write a program to provide detail of danger using human body temp. 
Minimum survivable: ~24–25 °C (75–77 °F)
Maximum survivable: ~42–43 °C (107–109 °F)
Normal safe range: ~36–37.5 °C (96.8–99.5 °F)
'''
try:
    temp = int(input("Enter your body temprature"))
    if temp<=74 or temp>=110:
        raise ValueError
    else:
        if temp>=75 and temp<=77:
            print("you body temprature is in Minimum survivable range")
        elif temp>=100 and temp<=109:
            print("you body temprature is in Maximum survivable range")
        elif temp>=96 and temp<=99:
            print("your body temprature is in safe range")
except ValueError as e:
    print("your body temprature is quite unusal")
    print(type(e))
    print("Message:", str(e)) 