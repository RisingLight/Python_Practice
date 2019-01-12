print("\n\nQ. From the string input, count the special characters, alphabets, digits, lowercase and uppercase characters.\n\n")
digit=0
alpha=0
ch=0
lower=0
upper=0


inp= input("Enter String: ")
for i in inp:
    if(i.isalpha()):
        alpha+=1
    elif(i.isnumeric()):
        digit+=1
    if(i.isupper()):
        upper+=1
    if(i.islower()):
        lower+=1
    else: ch+=1
print("Digit: {0}\nAlphabets: {1}\nSpecial Characters: {2}\nLowercase: {3}\nUppercase: {4}".format(digit,alpha,ch,lower,upper))
