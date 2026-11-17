def convt(k):
    p=k*2.2
    return p
def ptokg(p):
    k=p/2.2
    return k

k=float(input('enter weight in kg:'))
r=convt(k)
print(f"kg to pound:{r:.2f}")
p=float(input('enter weight in pound:'))
s=ptokg(p)
print(f"pound to kg:{s:.2f}")