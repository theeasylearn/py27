#create function that return total minutes from given hours and given minutes 
# with return value with argument function
def toMinutes(hours,minutes):
    TotalMinutes = (hours * 60) + minutes
    return TotalMinutes


hours = int(input("Enter hours"))
minutes = int(input("Enter minutes"))

TotalMinutes = toMinutes(hours,minutes)
print(f"total minutes = {TotalMinutes}")
