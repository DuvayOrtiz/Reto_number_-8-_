#punto6
n=int(input("ingresar n: "))
b = float(input("base: "))
def factorial(n,b):
    p = 1
    for i in range(1,n+1):
        p *= b
    return p
print(factorial(n,b))