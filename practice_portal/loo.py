p=0
n=0
while True:
    num=int(input("numbr:"))
    if num==0:
        break
    else:
        if num>0:
            p=p+1
        else:
            n=n+1
print(f"positive numbr:{p}\nnegative numbers:{n}")




sum=0
total=0
while True:
    num=int(input("numbr"))
    if num<=0:
        break
    else:
        sum+=num
        total+=1
print(f"avg:{sum/total}")