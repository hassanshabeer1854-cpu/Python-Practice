def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print("factor",i)

n=int(input("ntr numbr:"))
factor(n)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)


n=int(input("ntr numbr:"))
factorial(n)