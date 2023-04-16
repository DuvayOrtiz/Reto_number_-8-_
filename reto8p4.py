#punto 4
n=int(input("ingresar n: "))
s=[]
f=[]
def factorial(n : int ):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p

def factorialdenumeros(n):
    for i in range(1,n+1):
        s.append(i)
    for i in range(1,n+1):
        f.append(factorial(i))
    return s,f
print(factorialdenumeros(n))