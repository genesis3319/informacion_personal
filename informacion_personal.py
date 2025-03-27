# Creamos un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Aidan Torres",
    "edad": 22,
    "ciudad": "Madrid",
    "profesion": "Doctor"
}

# Accedemos al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Barcelona"

# Agregamos una nueva clave-valor al diccionario que represente el "telefono"
informacion_personal["telefono"] = "612345644"

# Verificamos si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["telefono"] = "612345644"

# Eliminamos la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)