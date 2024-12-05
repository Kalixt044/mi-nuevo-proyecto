# 1. Lista de estudiantes y bucle para mostrarlos
estudiantes = ["Juan", "María", "Pedro", "Ana"]

print("Estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# 2. Diccionario de contactos y mostrar claves y valores
contacto = {
    "nombre": "Carlos",
    "correo": "carlos@example.com"
}

print("\nContactos:")
for clave, valor in contacto.items():
    print(clave, ":", valor)

# 3. Agregar elementos a una lista y actualizar valores en un diccionario
# Lista de frutas
frutas = ["manzana", "banana"]

nueva_fruta = input("Ingrese una nueva fruta: ")
frutas.append(nueva_fruta)
print("Lista actualizada:", frutas)

# Diccionario de personas
personas = {"nombre": "Ana", "edad": 30}

nuevo_dato = input("Ingrese un nuevo dato (ejemplo: edad=35): ")
clave, valor = nuevo_dato.split("=")
personas[clave] = valor
print("Diccionario actualizado:", personas)
