q=input()
a,n=0,0
for i in q:
    if(i.isnumeric()):
        n=n+1
    elif(i.isalpha()):
        a=a+1
    else:
        continue
if(a>0 and n>0):
    print("Yes")
else:
    print("No")
