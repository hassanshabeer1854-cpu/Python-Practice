def bmi(p,h):
   '''this fun is usee to calculate BMI'''
   BMI=p*703/h**2
   print(f"BMI:{BMI:.2f}")
   if BMI<18.5:
      return "underage"
   elif BMI>18.5 and BMI<24.9:
      return "normal"
   elif BMI>24.9 and BMI<29.9:
      return "overiegth"
   else:
      return "obesee"


p=float(input("enter pound:"))
h=float(input("enter height:"))
r=bmi(p,h)
print(f"accoring to BMI you are:{r}")