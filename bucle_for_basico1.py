# 1. Básico: números del 0 al 100
print("=== 1. Básico ===")
for numero in range(101):
    print(numero)

# 2. Múltiplos de 2 entre 2 y 500
print("=== 2. Múltiplos de 2 ===")
for numero in range(2, 501, 2):
    print(numero)

# 3. Contando Vanilla Ice
print("=== 3. Contando Vanilla Ice ===")
for numero in range(1, 101):
    if numero % 10 == 0:
        print("baby")
    elif numero % 5 == 0:
        print("ice ice")
    else:
        print(numero)

# 4. Suma de números pares del 0 al 500,000
print("=== 4. Número gigante ===")
total = 0
for numero in range(0, 500001, 2):
    total += numero
print(total)

# 5. Cuenta regresiva desde 2024 de 3 en 3
print("=== 5. Regrésame al 3 ===")
for numero in range(2024, 0, -3):
    print(numero)

# 6. Contador dinámico
print("=== 6. Contador dinámico ===")
numInicial = 3
numFinal = 10
multiplo = 2
for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)