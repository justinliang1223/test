def R():
    import math
    a,b,c,d=map(float,input().split())
    A=pow(a-c,2)
    B=pow(b-d,2)
    ANS=math.sqrt(A+B)
    return(print(format(ANS,'.3f')))
R()