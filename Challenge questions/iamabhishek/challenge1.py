string = input("Enter a string: ")
splittedString = string.split(" ")

capStringWithoutSpace= ""
for i in splittedString:
    capStringWithoutSpace= capStringWithoutSpace + i.capitalize()
    
print("Capitalized String with space: " + string.title())
print("Capitalized String without space: " + capStringWithoutSpace)

wordList= []
count = -1
lengthOfString=  len(capStringWithoutSpace)
for i in capStringWithoutSpace:
    count+=1
    if(count==0):
        if(i.isupper()):
            leftLimit=count
    elif(i.isupper()):
        rightLimit=count
        wordList.append(capStringWithoutSpace[leftLimit:rightLimit])
        leftLimit=rightLimit
    elif(count==lengthOfString-1):
        rightLimit=count+1
        wordList.append(capStringWithoutSpace[leftLimit:rightLimit])
       
concatenatedString = " ".join(wordList)
lengthOfConcatenatedString = len(concatenatedString)
formattedString= concatenatedString[0].capitalize()+concatenatedString[1:lengthOfConcatenatedString].lower()
print(formattedString)

