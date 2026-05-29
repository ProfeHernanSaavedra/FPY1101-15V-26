diccionario = {}

diccionario = {
    "Rut" : "123-4",
    "Nombre" : "Alam Brito",
    "Direccion" : "Viña",
    "edad" : 23,
    "fonos" : [1234,5678,88765]
}

print(f"Nombre: {diccionario["Nombre"]}")
print("Dirección: ",diccionario["Direccion"])

print("Telefono 2 : ",diccionario["fonos"][1])

diccionario["correo"] = "aaa@aaa.com"
print(diccionario)

diccionario["correo"] = "alam@gmai.com"
print(diccionario)

del diccionario["correo"]
print(diccionario)


