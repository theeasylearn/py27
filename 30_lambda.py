#example of lambda function (must be single line and no need of return )
getInterest = lambda amount,rate, year: (amount * rate * year) / 100
getSquare = lambda num: num * num 
getQube = lambda num: getSquare(num) * num 

amount = int(input("Enter amount"))
rate = int(input("Enter rate"))
year = int(input("Enter year"))

num = int(input("Enter number to get square and qube"))

print(getInterest(amount,rate,year))
print(getSquare(num))
print(getQube(num))