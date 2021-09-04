#cadenaNumeros = input("Ingrese cadena de numeros: ")
numeros = []
#print(cadenaNumeros)


#cadenaNumero = (cadenaNumeros.split("*"," "))
cadenaNumeros ="12*3 *4"
numeros = [int(temp) for temp in cadenaNumeros.split() if temp.isdigit()]
print(numeros)
#print(cadenaNumero)
'''
for i in cadenaNumeros:
    if i.isnumeric():
        print('si'+ str(i))
    
'''