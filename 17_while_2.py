'''

write a program to print following pattern 
*
* * 
* * *
* * * *
* * * * *
'''
line = 1
while line<=5: #outer loop
    astrik = 1
    while astrik<=line: #inner loop 
        print(f"*",end=' ')
        astrik=astrik+1
    print("") #for new line
    line+=1