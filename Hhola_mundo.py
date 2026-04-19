# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Andrea"
nombre = "Andrea"
print("Hola,", nombre)        # con coma
print("Hola, " + nombre)      # con +

# 3. Imprime "Hola 7!" (o tu número de la suerte)
numero = 7
print("Hola", numero, "!")           # con coma
print("Hola " + str(numero) + "!")   # con + (str() es la corrección del error)

# 4. Imprime "¡Me encanta comer sushi y empanadas!"
comida1 = "sushi"
comida2 = "empanadas"
print("¡Me encanta comer {} y {}!".format(comida1, comida2))  # con .format()
print(f"¡Me encanta comer {comida1} y {comida2}!")            # con f-string