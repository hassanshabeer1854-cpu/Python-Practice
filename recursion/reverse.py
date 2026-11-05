def rvrs(s):
    if len(s)==0:
        return ""
    return rvrs(s[1:])+s[0]
r=rvrs("hassan")
print(r)