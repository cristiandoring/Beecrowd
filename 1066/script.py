contador_pares = contador_impares = contador_positivos = contador_negativos = 0
for i in range(1,6):
    numero = int(input(''))
    if numero % 2 == 0:
        contador_pares += 1
    elif numero % 2 == 1:
        contador_impares += 1
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
print(f'{contador_pares} valor(es) par(es)')
print(f'{contador_impares} valor(es) impar(es)')
print(f'{contador_positivos} valor(es) positivo(s)')
print(f'{contador_negativos} valor(es) negativo(s)')