print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos un diccionario con las asignaturas y sus respectivos créditos
asignaturas_creditos = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

# Inicializamos una variable para almacenar el total de créditos
total_creditos = 0

# Iteramos sobre el diccionario para mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas_creditos.items():
    # Mostramos la información en el formato solicitado
    print(f"{asignatura} tiene {creditos} créditos.")
    # Sumamos los créditos al total
    total_creditos += creditos

# Mostramos el total de créditos del curso
print(f"El número total de créditos del curso es: {total_creditos}")
