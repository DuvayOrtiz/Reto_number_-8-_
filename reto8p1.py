#punto 1
x : int = 0
y = x**2
for i in range(101):
    print(x,y, sep=":")
    x+=1
    y=x**2