def ckprime(a):
    if a> 1:
        for i in range(2, a):
            if (a % i) == 0:
                break
        else:
            li.append(a)

a,b=map(int,input().split(" "))
li=[]
for i in range(a+1,b):
    ckprime(i)
for i in range(len(li)):
    if(i==len(li)-1):
        print(li[i],end="")
    else:
        print(li[i],end=" ")
    
