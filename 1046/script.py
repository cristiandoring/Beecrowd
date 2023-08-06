a,b = map(int,input('').split())

if a == b:
    duracao = 24
elif a > b:
    duracao = b + (24 - a)
elif a < b:
    duracao = b - a
print(f'O JOGO DUROU {duracao} HORA(S)')