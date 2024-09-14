t = int(input(""))

respostas = list(map(int, input("").split()))

contador = 0

for resposta in respostas:
    if resposta == t:
        contador += 1
print(contador)
