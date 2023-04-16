#punto10
import math
def arctan(x):
    return math.atan(x) 
def seriemcpollo(x,n):
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)+1))/((2*i)+1)
    return m
x=float(input("ingresar x entre -1 y 1: "))
n=int(input("ingresar cantidad de las serie de Maclaurin : "))
print(arctan(x))
print(seriemcpollo(x,n)) 