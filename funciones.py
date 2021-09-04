print("CRUD Adminstrar Contactos")



menu = True

while menu:
    opcion = input('Menu de opciones \n1. Crear un contacto \n2. Leer todos los contactos \n3. Actualizar un contacto \n4.  Eliminar un contacto \n')
    persona = {}
    if  int(opcion) > 0 and int(opcion) < 5:
        if  int(opcion) > 0:
            persona = {
                'nombre ' : input('Ingrese el nombre \a'),
                'apellido' : input('Ingrese celular\n'),
                'celular' : input('ingrese Correo electronico\n')
            }
        elif int(opcion) > 1:
            print(persona)
        elif int(opcion) > 2:
            actualizar =input("Que usuario desea editar \nIngrese nombre")
            
            
            
    else:
        print("nmero erroneo")
        
