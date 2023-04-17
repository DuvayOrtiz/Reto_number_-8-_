#punto 3
x=int(input("ingresar numero mayor igual que 2: ")) 
def pares(x):
    c = []
    for i in range(1,x+1):
        if i%2==0:
            c.insert(0,i)
    return c
print(pares(x))
print("listo")
