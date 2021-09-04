a = 2
b = 4



def multiplicacion(a,b):
    producto = 0
    while b!=0:
        producto = producto+a
        b=b-1
    #print(producto)
    return producto

resultado = multiplicacion(a,b)
print(resultado)