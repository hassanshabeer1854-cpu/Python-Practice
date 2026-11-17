for i in range(1,10):
    if i%2!=0:
        print(i)



s=int(input("start numbr"))
n=int(input("entr numbr:"))
for i in range(s,n+1):
    print(i)


import string as s
for i in s.ascii_letters:
    print(i)



#rvsr alphabat an vovl nai hon ga
import string as s
a = list(s.ascii_lowercase)
a.reverse()
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
      continue
    print(i)

