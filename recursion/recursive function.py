def sum(n):
    if n==0:
        return 0
    l=n%10
    return l+sum(n//10)
s=sum(99)
print(s)