N = int(input(''))

for i in range(0,N):
    n1,n2 = map(int,input('').split())

    if n2 == 0:
        print('divisao impossivel')
    else:
        print(f'{n1/n2:.1f}')