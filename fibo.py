a=int(input())
p,q,r=0,1,0
li=[]
print(p+q,end=" ")
for i in range(a-1):
    r=p+q
    p=q
    q=r
    li.append(r)
for i in range(len(li)):
    if(i==len(li)-1):
        print(li[i],end="")
    else:
        print(li[i],end=" ")
