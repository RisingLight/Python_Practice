def bin(instrlist):
    #instr=input("Enter your String ")
    #instrlist=instr.split()
    # print(instrlist)
    a=eval(instrlist[0])
    b=eval(instrlist[-1])
    if '==' in instrlist:
        if(a==b):
            print(1)
        else:
            print(0)
    if '!=' in instrlist:
        if(a!=b):
            print(1)
        else:
            print(0)
    if '>=' in instrlist:
        if(a>=b):
            print(1)
        else:
            print(0)
    if '<=' in instrlist:
        if(a==b):
            print(1)
        else:
            print(0)

listinstr=input("enter your input")
listinstr=listinstr.split()
# print(listinstr)
for i in range(0,len(listinstr),3):
    # print(i,999)
    # print(listinstr[i:i+3])
    bin(listinstr[i:i+3])
