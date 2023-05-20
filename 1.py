import sys
sys.setrecursionlimit(100000)
def R(a,b,c):  
    if c<=1:
        return 1
    elif a%c==0 and b%c==0:
        return c 
    else :
        return R(a,b,c-1)
a,b=map(int,input().split())
if a>b:
    c=a
else:
    c=b
R(a,b,c)
print(R(a,b,c))