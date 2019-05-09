
def ab(x):
    import math 
    m,n,M=0,0,0
    while m<1000000:
        M=(2*m+1)*math.pi/2
        n=n+2/M*math.sin(M)*math.exp(-M**2*x)
        m=m+1
    return n
print("hello")  
