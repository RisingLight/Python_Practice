extract=[]
def mod(a,modnum):
    global extract
    left=0
    addnum=0
    for i in range(0,modnum):
        if((modnum-a*i)>0):
            left=i
            addnum=modnum-a*i
            continue
        break
    if(addnum != 1):
        extract.append(mod(addnum,a))
    return left,addnum

print(mod(11,26))
print(extract)
            
    
