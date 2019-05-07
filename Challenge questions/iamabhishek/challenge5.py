import sys

def check(a,b,c):
    if(b== "=="):
        if(a==c):
            return 1
        else:
            return 0
    elif(b=="<="):
        if(a==c or a<c):
            return 1
        else:
            return 0
    elif(b==">="):
        if(a==c or a>c):
            return 1
        else:
            return 0    

m=sys.stdin.read().splitlines()
for i in m:
    a,b,c = i.split()
    d=check(a,b,c)
    print(d,end="\n")