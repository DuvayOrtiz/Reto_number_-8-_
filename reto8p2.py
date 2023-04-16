#punto 2
x=[]
y=[] # Se crean los conjuntos que se van a llenar con lo pedido
for i in range(1001): # Se establecen los rangos y se da la orden
    if i%2==0:
        x.append(i)
for i in range(1001): 
    if i%2!=0:
        y.append(i) # Dependiendo del residuo se agrega a su conjunto
print(x)
print(y) # Se imprimen los conjuntos con los números
print("listo")