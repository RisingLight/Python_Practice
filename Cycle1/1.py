lis=[6,5,2,1,6,4]
m=max(lis)
full=0
for i in lis:
    if(i>full and i!=m):
        full=i
print(full)
