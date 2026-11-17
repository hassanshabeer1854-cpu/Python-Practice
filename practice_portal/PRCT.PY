def p(o,t):
    '''this fun is usd to calculat prctag'''
    prcntage=(o/t)*100
    return prcntage


c=input("enter course name:")
o=int(input('enter obtain marks:'))
t=int(input('enter total marks:'))
r=p(o,t)
print(f"prctag in {c} :{r}")