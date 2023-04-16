#punto8
import math
def expo(x):
    return  math.exp(x) 
def factorial(n : int ):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemcgallo(x,n):
    m=0
    for i in range(n+1):
        m += (x**i)/factorial(i)
    return m

x=float(input("ingresar x: "))
n=int(input("ingresar cantidad de las serie de Maclaurin : "))
print(expo(x))
print(seriemcgallo(x,n))