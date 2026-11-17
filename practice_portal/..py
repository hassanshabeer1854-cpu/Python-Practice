def book(b):
    point=0
    match b:
        case 0:
            point=0
        case 1:
            point=5
        case 2:
            point=15
        case 3:
            point=30
        case 4:
            point=60
        case _:#ya is liya ka koi v valu match na kra to ya run hota
            point=0
    return point
            
            
b=int(input("enteer book you purchase in this month:"))
r=book(b)
print(f"you purchase {b} books \nso your points:{r} ")