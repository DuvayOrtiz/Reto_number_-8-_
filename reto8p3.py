#punto 3
x=int(input("ingresar numero mayor igual que 2: ")) 
def pares(x):
    c = []
    for i in range(x+1):
        if i%2==0:
            c.append(i)
    return c
print(pares(x))
print("listo")