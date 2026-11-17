num=int(input("intr numbr:"))
l=[]
while num>0:
    n=num%10
    l.append(n)
    num=num//10
l.reverse()
for i in l:
    print(i)

