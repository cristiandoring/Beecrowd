
while True:
    M, N = map(int, input('').split())

    soma=0
    if M <= 0 or N <= 0:
        break
    else:
        if M < N:
            for i in range(M,N+1):
                print(f'{i} ', end="")
                soma += i
            print(f'Sum={soma}')
        elif M > N:
            for i in range(N,M+1):
                print(f'{i} ', end="")
                soma += i
            print(f'Sum={soma}')
        else:
            print(f'{M} Sum=0')