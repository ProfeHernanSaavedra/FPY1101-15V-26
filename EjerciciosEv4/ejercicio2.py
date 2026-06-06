def agregar_alumno(alumnos):
    '''en esta funcion ingresaremos un nombre alumno con sus notas'''
    nombre = input("Ingrese nombre del alumno: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    if nombre in alumnos:
        print("El alumno ya existe")
        return
    
    if nombre.isdigit():
        print("El nombre debe ser con letras! ")
        return
    
    cantidad = int(input("Ingrese cantidad de notas: "))

    notas = []

    for i in range(cantidad):
        print(f"Ingresando nota {i+1}/{cantidad}")
        notaParcial = validaNota()
        notas.append(notaParcial)

    alumnos[nombre] = notas    
    print("Alumno agregado correctamente!")


def validaNota():
    while True:
        try:
            nota = float(input("Ingrese nota: "))
            if nota >=1.0 and nota <= 7.0:
                return nota
            else:
                print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("Debe ingresar un valor válido!")


alumnos = {}

while True:
    print("-- MENU ALUMNOS---")
    print("1. Agregar Alumnos")
    print("2. Mostrar Alumnos")
    print("3. Ver Promedio")
    print("4. Mejor Alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")

    while True:
        try:
            op = int(input("Inrese su opción: "))
            break
        except ValueError:
            print("Por favor ingrese un valor válido, intente nuevamente")
    
    if op == 1:
        agregar_alumno(alumnos)
        # dato = input("Ingrese dato: ")
        # print(dato.isdigit())
        # if dato.isdigit():
        #     print("debe ser letras")
        # else:
        #     print("Correcto! ") //para hacerlo con todas las lineas use ctr + }
    elif op == 2:
        print(alumnos)
    
    

