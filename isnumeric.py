q=(input())
c,o=0,0
for i in q:
    if(i.isnumeric()):
        c=c+1
    else:
        o=o+1
if(c>0 and o==0):
    print("yes")
elif(c>0 and o==1):
    print("yes")
else:
    print("no")
