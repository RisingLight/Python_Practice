def print_without_spaces(some_str):
    flag = 0
    other_str=""
    for i in some_str:
        if flag == 0 and i!=" ":
            other_str+=i
        elif i==" ":
            flag=1
        elif flag==1 and i!=" ":
            flag=0
            i=i.upper()
            other_str+=i

    return other_str
def print_with_spaces(some_str):
    flag=0
    other_str=""
    for i in some_str:
        if i>="A" and i<="Z":
            flag=1

        if flag==0 and i!=" ":
            other_str+=i


        if flag == 1:
            i=i.lower()
            flag=0
            other_str+=" "
            other_str+=i

    other_str = other_str[1].capitalize()+other_str[2:]

    return other_str


some_str=input("Enter the string : ")
some_str=print_without_spaces(some_str)
print(some_str)
print(print_with_spaces(some_str))

