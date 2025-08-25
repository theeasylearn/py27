amount = 1000
def updateAmount(rupees):
    # amount = 0 #local variable
    global amount
    # it will update local variable
    amount = amount + rupees
    print("amount in function",amount)


print("global amount ",amount) # 1000
updateAmount(99)
print("global amount ",amount) # 1000
