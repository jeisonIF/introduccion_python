'''
    MOstar numero de letras que se repite de una cadena de texto
'''
cadenaIngreso = input('Ingrese cadena de texto: \a')


res = {}
resultado = {}
letrasUnicas= []
for caracter in cadenaIngreso:
        if caracter in res.keys():
            res[caracter] = res[caracter] + 1
        else:
            res[caracter] = 1

for letra in cadenaIngreso:
    if resultado.get(letra):
        resultado[letra] += 1
    else:
        resultado[letra] =1
print(res)
print(resultado)

for letra in cadenaIngreso:
    cont = 0
    for letraUnica in letrasUnicas:
        if letraUnica == letra:
            cont += 1
        if cont == 0:
            letrasUnicas.append(letra)

for letrasUnica in letrasUnicas:
    print(letraUnica, texto.count(letraUnica))
                

