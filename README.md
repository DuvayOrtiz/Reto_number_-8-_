# Reto_number_-8-_
# Haciendo el reto 8, SIUUUUUUUUUUUUUUU :D
# Reto__8__

## *Ejercicios* :ok_hand:

### Num1 :trollface:
- Ejercicio: Qué se genera con range(-2)?

se crea un conjunto vacío.

## *Punto 1*:dog:
- Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```ruby
#punto 1
x : int = 0
y = x**2  # Establecemos las variables  
for i in range(101): # Establecemos el rango
    print(x,y, sep=":") # Imprimimos las variables en el rango
```

## *Punto 2* :cat:
- Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```ruby
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
```

## *Punto 3* :tiger:
- Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```ruby
#punto 3
def pares(x): # Definimos unas función  para ir hasta x
    c = [] # Hacemos un conjunto
    for i in range(x+1): # Establecemos el rango y unimos al conjunto
        if i%2==0:
            c.append(i)
    return c
x=int(input("ingresar numero mayor igual que 2: "))  # Pedimos x para ir hasta ahí
print(pares(x)) # Imprimimos 
print("listo")
```


## *Punto 4* :koala:
- Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```ruby
#punto 4
s=[] # Hacemos los dos conjutos que se piden
f=[]
def factorial(n : int ): # Hacemos la función de factorial
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def factorialdenumeros(n): 
    for i in range(1,n+1):  #llenamos un conjunto con  n
        s.append(i)
    for i in range(1,n+1): # Llenamos el otro con factorial
        f.append(factorial(i))
    return s,f
n=int(input("ingresar n: ")) # Pedimos el n que va a definir el rango
print(factorialdenumeros(n)) # Imprimimos 
```

## *Punto 5* :penguin:
- Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```ruby
#punto 5
def pot2(n : int ): # Definimos la función
    p = 1 # Hacemos una variable
    for i in range(1,n+1): # Hacer el rango hasta n
        p *= 2
    return p 
n=int(input("ingresar n: ")) # Pedir la n hasta la que se eleva 2
print(pot2(n)) # Imprimo la respuesta
```
## *Punto 6* :frog:
- Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for
```ruby
#punto6
def factorial(n,b): # Definimos la función
    p = 1 # Hacemos una variable
    for i in range(1,n+1): # Hacer el rango hasta n
        p *= b 
    return p
b = float(input("base: ")) # Pedir la base
n=int(input("ingresar n: ")) # Pedir la n hasta la que se eleva la base
print(factorial(n,b)) # Se imprime 
```
## *Punto 7* :whale:
- Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```ruby
#punto7
for i in range(1,10): # Se hacen el rango de 1 hasta 9 que son las tablas
    for n in range(1,11): # Se hacen el rango de 1 hasta 10 
        print(i, "x", n, "=", i*n)  # Se imprime el producto de ambos rangos
```
## *Punto 8* :water_buffalo:
- Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

```ruby
#punto8 :turtle:
import math # Importamos la libreria math
def expo(x): # Hacemos una función con el exponencial
    return  math.exp(x) 
def factorial(n : int ): # Usamos el factorial 
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemcgallo(x,n): # Se hace conla serie Maclaurin la aproximación
    m=0
    for i in range(n+1):
        m += (x**i)/factorial(i)
    return m

x=float(input("ingresar x: ")) # Se pide el valor de x
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) #Se pide la cantidad de la serie
print(expo(x)) # Se imprime el valor "real"
print(seriemcgallo(x,n)) # Se imprime la aproximación
```
## *Punto 9*  :honeybee:
- Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

```ruby
#punto9
import math # Importamos la libreria math
def seno(x): # Hacemos una función con el seno
    return  math.sin(x) 
def factorial(n : int ): # Usamos el factorial 
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
def seriemcpollo(x,n): # Se hace con la serie Maclaurin la aproximación
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)+1))/(factorial((2*i)+1))
    return m

x=float(input("ingresar x: ")) # Se pide el valor de x
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) #Se pide la cantidad de la serie
print(seno(x)) # Se imprime el valor "real"
print(seriemcpollo(x,n)) # Se imprime la aproximación
```
## *Punto 10* 
- Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```ruby
#punto10 :elephant:
import math # Importamos la libreria math
def arctan(x): # Hacemos una función con el arcotangente
    return math.atan(x) 
def seriemcpollo(x,n): # Se hace con la serie Maclaurin la aproximación
    m=0
    for i in range(n+1):
        m += ((-1)**i)*(x**((2*i)+1))/((2*i)+1)
    return m
x=float(input("ingresar x entre -1 y 1: ")) # Se pide el valor de x entre -1 y 1
n=int(input("ingresar cantidad de las serie de Maclaurin : ")) #Se pide la cantidad de la serie
print(arctan(x)) # Se imprime el valor "real"
print(seriemcpollo(x,n))  # Se imprime la aproximación
```
#### *Eso es todo por hoy :D* _-Duva-_ :sunflower: :tulip:
