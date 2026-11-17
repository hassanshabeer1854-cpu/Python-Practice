def convrt(c):
    Fahrenheit_temperatures=(c*9)/5+32
    return Fahrenheit_temperatures


c=int(input('enter Celsius temperatures'))
r=convrt(c)
print(r)