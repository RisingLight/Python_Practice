numberOfRows = int(input("Enter numberOfRows: "))
stringVal = input("Enter String: ")
length = len(stringVal)
numberOfColumn = numberOfRows*3


stringLine = int(numberOfRows/2)

pattern= ".|."
dash = "-"


def printW(num):
    print(dash* int(num))
    
def printPattern(i):
    pattSize = len(pattern*i)
    w = (numberOfColumn-pattSize)/2
    a= dash* int(w)+ pattern *i + dash* int(w)
   # if(i>stringLine+1):
   #     return
   # if(len(a)<=numberOfColumn):
    print(a)
    
    #else:
       # print(dash* int(w)+ pattern *(i-int((len(a)-numberOfColumn)/2)) + dash* int(w))


def printStr(i):
    w= len(stringVal)
    print(dash* int((numberOfColumn-w)/2) + stringVal + dash* int((numberOfColumn-w)/2))
    i-=2
   
def run():
    i=1
    while( i<=stringLine+1):
        printPattern(i)
        i+=2
    printStr(i)
    while(i>=1):
        printPattern(i)
        i-=2
    
run()
