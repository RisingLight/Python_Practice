#rail fence

string=input("Enter the string :")
part1,part2='',''
i=1
if(len(string)%2!=0):
    string+=" "
while(i<len(string)):
    part1+=string[i-1]
    part2+=string[i]
    i=i+2
print(part1+part2)

newString=part1+part2
newpart1=newString[0:len(newString)//2+1]
newpart2=newString[len(newString)//2:]

i=1
backString=''
while(i<max(len(newpart1),len(newpart2))):
    backString=backString+newpart1[i-1]+newpart2[i-1]
    i+=1
print(backString)
