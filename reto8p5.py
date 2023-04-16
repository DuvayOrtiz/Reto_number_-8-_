#punto 5
n=int(input("ingresar n: "))
def pot2(n : int ):
    p = 1
    for i in range(1,n+1):
        p *= 2
    return p
print(pot2(n))