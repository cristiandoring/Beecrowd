N = float(input(''))

if N >= 0 and N <= 25:
    print('Intervalo [0,25]')
elif N > 25 and N <=50:
    print('Intervalo (25,50]')
elif N > 50 and N <=75:
    print('Intervalo (50,75]')
elif N > 75 and N <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')