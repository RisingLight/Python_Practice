import random
import os
def shuf(string):
    ltemp=string[1:len(string)-1]       # taking only the mid part { change it into string[0:len(string)] for a full words shuffle
    ltemp=list(ltemp)                   # convert the word into alphabet list eg: "hey" -> ["h","e","y"]
    random.shuffle(ltemp)               # shuffles the alphabet
    ltemp="".join(ltemp)                # join the alphabet back to a word
    ltemp=string[0]+ltemp+string[len(string)-1]     # add the first and the end alphabet to the word
    return ltemp                                # returns the shuffled word

def filewrite(stext):
    f=open("output.txt","w")
    f.write(stext)
    

def wordscramble():
    #f=open("word.txt","r")
    fn=input("Enter file name:")
    f=open(fn,"r")
    text=f.read()
    print("The text before scrambling:", text)
    text=text.split()               # this splits words from string        
    stext=[]                        #scramble list { empty }
    for i in range(len(text)):
        stext.append(shuf(text[i])) # shuffles the word mid part only , starting and ending alphabets are not touched
    stext=" ".join(stext)
    print("The text after scrambling:")                            # joins the words into a string again
    print(stext)
    filewrite(stext)
    

     
wordscramble()  # scramble's the file text 


