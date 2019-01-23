
def q3():
    string=input(" Enter your String :- ")
    set=int(input(" Enter your Slice size:- "))
    count=0
    while(count<len(string)):
        print(string[count:count+set])
        count+=set

q3()
