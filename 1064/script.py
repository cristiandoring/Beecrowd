contador = soma = 0
for i in range(1,7):
    numero = float(input(''))

    if numero > 0:
        contador += 1
        soma += numero
print(f'{contador} valores positivos')
print(f'{soma/contador:.1f}')