#create function that return total minutes from given hours and given minutes 

# without return value without argument 
def printLine():
    print("_"*110)
    
#without return value with argument 
def printLetter(letter,count):
    print(letter*count)
# with return value with argument function

def getMinutes():
    minutes = 60
    return minutes

def toMinutes(hours,minutes):
    TotalMinutes = (hours * 60) + minutes
    return TotalMinutes

printLine()
hours = int(input("Enter hours"))
minutes = int(input("Enter minutes"))
printLine()


TotalMinutes = toMinutes(hours,minutes)
printLetter('*',100)
print(f"total minutes = {TotalMinutes}")
printLetter('^',110)
