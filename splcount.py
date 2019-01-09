s=input()
c=0
for i in s:
    if(i.isnumeric()):
        continue
    elif(i.isalpha()):
        continue
    elif(i.isspace()):
        continue
    else:
        c=c+1
print(c)
