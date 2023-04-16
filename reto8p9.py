#punto9
import math
def seno(x):
    return  math.sin(x) 
def factorial(n : int ):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemcpollo(x,n):
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)+1))/(factorial((2*i)+1))
    return m

x=float(input("ingresar x: "))
n=int(input("ingresar cantidad de las serie de Maclaurin : "))
print(seno(x))
print(seriemcpollo(x,n))