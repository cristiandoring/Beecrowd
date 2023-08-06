a,b,c,d = map(int,input('').split())

minutos = horas = 0

if c - a == 1:
    if b > d:
        minutos = d + (60 - b)
        
    elif d > b:
        minutos = d - b

else:
    if a > c:
        horas = c + (24 - a)
    elif a < c:
        horas = c - a
    if b > d:
        minutos = d + (60 - b)
        horas -= 1
    elif d > b:
        minutos = d - b
    if a == c:
        horas = 24
        minutos = 0
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')