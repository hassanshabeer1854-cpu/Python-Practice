def area(x,y):
    '''this function calculate area'''
    a=(1/2)*x*y
    return a


x=int(input('enter adjacent' ))
y=int(input('enter opposite'))
r=area(x,y)
print(f"area:{r}")