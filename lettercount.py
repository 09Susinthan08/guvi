def ck():
    su=0
    s = input()
    words = s.split()
    for i in range(0,len(words)):
        b=len(words[i])
        su=su+b
    print(su)
ck()
