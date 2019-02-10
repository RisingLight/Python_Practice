n = int(input("Enter N: "))
m = n*3

s = input("Enter String: ")
mid = int(n/2)

patt= ".|."
dash = "-"
length = len(s)

def printW(num):
    print(dash* int(num))

def f1(i):
    pattSize = len(patt*i)
    w = (m-pattSize)/2
    a= dash* int(w)+ patt *i + dash* int(w)
    if(len(a)<=m):
        print(a)
    else:
        print(dash* int(w)+ patt *(i-int((len(a)-m)/2)) + dash* int(w))


def printStr():
    w= len(s)
    print(dash* int((m-w)/2) + s + dash* int((m-w)/2))
   
def run():
    i=1
    while( i<int(m/2)):
        f1(i)
        i+=2
    printStr()
    i-=2
    while(i>=1):
        f1(i)
        i-=2
    
run()
