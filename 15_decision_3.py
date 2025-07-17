'''
    write a program to calculate & display gross annual income, tax and net income from monthly given income as per below income tax rule 
    annual income                           Tax Rate
    Above Rs. 24,00,001	                    30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,001 to Rs. 16,00,000	    15%
    below 12,00,000                          0%
'''
monthly_income = int(input("Enter monthly income"))
#calculate annual income 
annual_income = monthly_income * 12 
tax = 0 
if annual_income>24000001:
    tax = (annual_income * 30) / 100
elif annual_income>2000001:
    tax = (annual_income * 25) / 100      
elif annual_income>1600001:
    tax = (annual_income * 20) / 100      
elif annual_income>1200001:
    tax = (annual_income * 15) / 100      
else:
    tax = 0

net_income = annual_income - tax 
print(f"Gross Income {annual_income} tax = {tax} net income = {net_income}")
