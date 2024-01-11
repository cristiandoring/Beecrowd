N = int(input())

elementos = []

i = 1

while len(elementos) < 3*N:
    if i % 4 != 0:
        elementos.append(i)
    i += 1

for posicao, elemento in enumerate(elementos):
    if (posicao) % 3 == 0:
        if posicao > 0:
           print('PUM')

    print(elemento, end=' ')
print('PUM')

