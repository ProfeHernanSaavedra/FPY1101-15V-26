usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

while True:
    print("---MENU---")
    print("1. Iniciar Sesión")
    print("2. Registrar Usuario")
    print("3. Salir")
    #while True:
    try:
        opcion = int(input("Ingrese su opcion: "))
        #break
    except ValueError:
        print("Error, debe ingresar un número")
        continue

    if opcion == 1 :
        
        if usuario1 == None and usuario2 is None and usuario3 == None:
            print("Debe ingresar un usuario antes de iniciar sesión")
            continue
        
        usuario = input("Ingrese usuario: ")
        contraseña = input("Ingrese contraseña: ")
        # gracias José Valdés, presionando alt+z  o \ --> ajusta la linea de codigo a la pantalla todo el código --gracias José 
        if (usuario == usuario1 and contraseña == contrasena1) or (usuario == usuario2 and contraseña == contrasena2) or (usuario == usuario3 and contraseña == contrasena3):
            print("Inicio de sesión correcta!")

            while True:
                print("--MENU DE USUARIO--")
                print("1. Realizar llamada")
                print("2. Enviar correo electrónico")
                print("3. Salir")

                try:
                    op = int(input("Seleccione una opción: "))
                except ValueError:
                    print("Error, debe ingresar un número!")
                    continue

                if op == 1 :
                    celular = input("Ingrese número del celular (9 dígitos, comience con 9): ")
                    if len(celular) == 9 and celular.startswith("9") and celular.isdigit():
                        print("llamando al celular: ",celular)
                    else:
                        print("Error, el número no es correcto!")
                
                elif op == 2 :
                    correo = input("Ingrese su correo: ")
                    valido = False
                    for caracter in correo :
                        if caracter == "@" :
                            valido = True
                    
                    if valido :
                        mensaje = input("Ingrese mensaje del correo:")
                        print(f"Correo enviado a {correo} con mensaje: {mensaje}")

                    else:
                        print("Error correo no válido!")
                
                elif op == 3:
                    print("Cerrar sesión")
                    break
                else:
                    print("Opción no válida")

    elif opcion == 2 :
        print("Registra usuario")
        nuevoUsuario = input("Ingrese nuevo usuario: ")
        nuevaContraseña = input("Ingrese nueva contraseña: ")

        if usuario1 is None :
            usuario1 = nuevoUsuario
            contrasena1 = nuevaContraseña
        elif usuario2 is None :
            usuario2 = nuevoUsuario
            contrasena2 = nuevaContraseña
        elif usuario3 is None :
            usuario3 = nuevoUsuario
            contrasena3 = nuevaContraseña
        else:
            print("Error al ingresar usuario, máximo 3")
    

    elif opcion == 3:
        print("Saliendo del sistema..")
        break
    else:
        print("Opción no válida!")

