#example of for each loop on tuples 
countries = (
    "Uzbekistan", "Poland", "Kazakhstan", "Greenland", "Japan",
    "Thailand", "Iceland", "Switzerland", "Morocco", "Tajikistan",
    "Spain", "Australia", "Kyrgyzstan", "Swaziland", "Pakistan",
    "Netherlands", "Brazil", "Norway", "Italy", "Finland",
    "Turkmenistan", "Bangladesh", "Argentina", "Ireland", "Afghanistan",
    "Egypt", "Azerbaijan", "Canada", "Germany", "New Zealand"
)
#display only that country which ends with land 
#also country countries with ends with tan 
count = 0 
for item in countries:
    if "land" in item:
        print(item)
    elif "tan" in item:
        count+=1
print(count)