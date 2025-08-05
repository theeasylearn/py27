def getTotalSeconds(hours,minutes=0,seconds=0):
    print(f"hours = {hours} minutes = {minutes} seconds = {seconds}")
    #local variable (variable declared inside function is called local variable)
    totalSeconds = hours * 60 * 60
    totalSeconds += minutes * 60
    totalSeconds += seconds
    return totalSeconds
h = 10
m = 30 
s = 15
totalSeconds = getTotalSeconds(h,m,s)
print(f"total seconds = {totalSeconds}")

totalSeconds = getTotalSeconds(h,m)
print(f"total seconds = {totalSeconds}")

totalSeconds = getTotalSeconds(h)
print(f"total seconds = {totalSeconds}")

#keywords arguments
totalSeconds = getTotalSeconds(minutes=m,seconds=s,hours=h)
print(f"total seconds = {totalSeconds}")