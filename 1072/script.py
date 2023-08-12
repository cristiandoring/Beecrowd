dentro = fora = 0
N = int(input(''))

for i in range(0,N):
    numero = int(input(''))
    if numero >= 10 and numero <= 20:
        dentro += 1
    else:
        fora += 1
print(f'{dentro} in')
print(f'{fora} out')