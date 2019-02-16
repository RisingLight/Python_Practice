# making of Caesar Cipher
seriesEnlv1=dict()
seriesDelv1=dict()
seriesEnlv2=dict()
seriesDelv2=dict()
def mapping():
    global seriesEnlv1
    global seriesDelv1
    global seriesEnlv2
    global seriesDelv2
    alphalv1='abcdefghijklmnopqrstuvwxyz'
    for i in range(0,26):
        seriesEnlv1[alphalv1[i]]=i
        seriesDelv1[i]=alphalv1[i]
    alphalv2='ZYXWVUTSRQPONMLKJIHGFEDCBA'
    for i in range(-26,0):
        seriesEnlv2[alphalv2[i]]=i
        seriesDelv2[i]=alphalv2[i]
    

def message(code):
    mess=[]
    ##print(code)
    global seriesDelv1
    global seriesDelv2
    for i in code:
        if(i>0 or i==0):
            mess.append(seriesDelv1[i])
        else:
            mess.append(seriesDelv2[i])
    return ("".join(mess))

def modify(string):
    splittedString = string.split(" ")
    capStringWithoutSpace= ""
    for i in splittedString:
        capStringWithoutSpace= capStringWithoutSpace + i.capitalize() 
    return capStringWithoutSpace

def remodify(string):
    wordList= []
    count = -1
    lengthOfString=  len(string)
    for i in string:
        count+=1
        if(count==0):
            leftLimit=count
        elif(i.isupper()):
            rightLimit=count
            wordList.append(string[leftLimit:rightLimit])
            leftLimit=rightLimit
        elif(count==lengthOfString-1):
            rightLimit=count+1
            wordList.append(string[leftLimit:rightLimit])
    concatenatedString = " ".join(wordList)
    lengthOfConcatenatedString = len(concatenatedString)
    formattedString= concatenatedString[0].capitalize()+concatenatedString[1:lengthOfConcatenatedString].lower()
    return formattedString

def textconv(text,key):
    mapping()
    key=key%26
    text=modify(text)
    code=[]
    global seriesEnlv1
    global seriesEnlv2
    for i in text:
        if(i.isupper()):
            code.append(-(abs(seriesEnlv2[i]-key)%26))
        else:
            code.append((seriesEnlv1[i]+key)%26)
    return (message(code))

def textrevert(encoded,key):
    code=[]
    key=key%26
    global seriesEnlv1
    for i in encoded:
        if (i.islower()):
            x=seriesEnlv1[i]- key
            if(x<0):
                x+=26
        else:
            x=seriesEnlv2[i]+ key
            if(x>0 or x==0 ):
                x-=26
        code.append(x)
    return remodify(message(code))

simpleText=input("Enter the simple text : ")
key=int(input(" Enter the key for the Text :"))
encoded=textconv(simpleText,key)
print(encoded)
decoded=textrevert(encoded,key)
print(decoded)


    

