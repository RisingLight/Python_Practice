str2 = input("Enter String")
n = int(input ("Enter Length"))
m = n*3
i = 1
lef = int(m/2) - 1
str1 = ".|."
while (i<n):
    print(lef*"-"+str1*i+lef*"-")
    i+=2
    lef-=3
l = len(str2)
rit = int((m-l)/2)
if(l%2==0):
    print(rit*"-"+str2+(rit+1)*"-")
else:
    print(rit*"-"+str2+rit*"-")
lef = lef+3
i-=2
while (i>=1):
    print(lef*"-"+str1*i+lef*"-")
    i-=2
    lef+=3
