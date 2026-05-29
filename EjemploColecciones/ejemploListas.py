datos = [] # inicialice la lista vacía

datos = [14,21,33,"Juan",33]
# pos    0   1  2    3

#J U A N
#0 1 2 3 --> posiciones

print(datos[1])
print()

for i in range(4):
    print(datos[i])

print()

for elemento in datos:
    print(elemento)

print(datos)

# agregar elemento a la lista datos

datos.append("Maria")
print(datos)
datos.insert(3,True)
print(datos)
print()
for elemento in datos:
    print(elemento)

print()
datos.remove(33)
print(datos)

print(datos.pop())
print(datos)

datos.pop(2)
print(datos)


datos.reverse()
print(datos)

datos2 = [43,2,32,1]
datos2.sort()
print(datos2)


datos.clear()
print(datos)
