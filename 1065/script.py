contador = 0
for i in range(1,6):
    numero = int(input(''))
    if numero % 2 == 0:
        contador += 1
print(f'{contador} valores pares')