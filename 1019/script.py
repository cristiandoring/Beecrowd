N = int(input(''))

horas = N//3600
minutos = (N//60)-horas*60
segundos = N-(horas*3600 + minutos*60)

print(f'{horas}:{minutos}:{segundos}')