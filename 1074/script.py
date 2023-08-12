N = int(input(''))

for i in range(0,N):
    numero = int(input(''))

    if numero % 2 == 0 and numero != 0:
        print('EVEN',end=' ')
    elif numero % 2 == 1:
        print('ODD',end=' ')
    

    
    if numero > 0:
        print('POSITIVE')
    elif numero < 0:
        print('NEGATIVE')
    else:
        print('NULL')
    