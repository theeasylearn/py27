import world as wd 
import india 
import sys 
#now we can use word wd instead of world 

print(wd.getAsianCountry())

print(wd.getAmericaCountry())

print(wd.getEuropianCountry())

print(india.getNorthStates())
print(india.getSouthStates())
print(india.getEastStates())
print(india.getWestStates())

sys.path.append("c:\\my_modules_2")
import languages as lang 
print(lang.getNorthLanguages())
print(lang.getSouthLanguages())
print(lang.getEastLanguages())
print(lang.getWestLanguages())