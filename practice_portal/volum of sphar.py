def volume():
    """this function is usd to calculat volum of sphr"""
    radius=float(input("enter radius:"))
    vol=(4/3)*3.1416*radius**3
    return vol
v=volume()
print(f"volum is {v}")