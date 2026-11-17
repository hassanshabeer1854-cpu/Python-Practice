print("\twelcome to calculator")
print("1.sum")
print("2.subtraction")
print("3.division")
print("4.multiplication")
print("5.average")
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))

c=int(input("enteer choice:"))
if c==1:
    print(f"sum:{num1+num2}")
elif c==2:
    print(f"subtraction:{num1-num2}")
elif c==3:
    if num2!=0:
      print(f"division:{num1/num2}")
    else:
        print("anything divid by 0 is 0")
elif c==4:
    print(f"multiplication:{num1*num2}")
elif c==5:
    print(f"average:{(num1+num2)/2}")
else:
    print("invalid numbr")
