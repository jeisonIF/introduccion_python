
'''
    int
    float
    str
    list => array mutable
    tupl => array inmutable
    dict => objeto
'''
numero1 = 10 #int
numero2 = 15.5 #float
nombre = "jeison" #str

#listas o arreglos => []
materias = ['Base de datos', 'Lenguaje de Cuarta Generacion']
listaNumeros = [1,2,3,4,5,6,7]
matrizEjemplo = [[1,2],[3,4]]
materias[0] = 'Programacion Avanzada!'
print(materias[0])
print(matrizEjemplo[1][0])

listaSinOrdenar = [10,15,2,-5,35]
print(listaSinOrdenar)
listaSinOrdenar.sort(reverse=True)
print(listaSinOrdenar)
listaSinOrdenar.sort(reverse=False)
print(listaSinOrdenar)

#tuplas => lista inmutable =>()
dias =('lunes','martes','miercoles','lunes','lunes','lunes')
print(dias[0])
# esta parte no se puede realizar dias[0] = 'kddk'

#boolean
esCorrecto = True
esCorrecto = False
print(len(materias))
print(len(dias))
print(dias.count('lunes'))

#dict =>{}
persona = {
    'nombre' : 'Jeison ',
    'apellido' : 'Iglesias',
    'edad' : 23,
    'materias' : ['lg','db'],
    'direccion':{
        'direccion':'Los guaduales',
        'ciudad' : 'Mocoa',
        'pais' : 'colombia'
    }
}
print(persona)
persona['apellido'] = 'Mavisoy'
print(persona['apellido'])
print(persona['materias'][1])
print(persona['direccion']['pais'])
persona['nombre_completo'] = persona['nombre']+' '+ persona['apellido']

#ciclos
for materia in materias:
    print('Este codigo pertenece al ciclo')
    print('Este tambien pertenece al ciclo')
    print(materia)

print('Este codigo No pertenece al ciclo')
'''
    operadores 
    +,
    -,
    *,
    /,
    %,
    **
'''
'''
    operadores logicos
    and,
    or,
    not
'''
'''
    Operadores relacionales
    <,
    >,
    ==,
    >,
    <=,
    !=
'''