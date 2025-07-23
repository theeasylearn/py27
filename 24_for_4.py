# concept of for loop on string variable 
word = input("enter any one word")
reverse = ''
for letter in reversed(word):
    #print(letter)
    reverse+=letter

if reverse == word:
    print("given word is palindrom")
else:
    print("given word is not palindrom")