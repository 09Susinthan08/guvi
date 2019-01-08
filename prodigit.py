a=int(input())
pro=1
while a>0:
    t=a%10
    pro=pro*t
    a=a//10
print(pro)
