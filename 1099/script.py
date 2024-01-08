N = int(input(''))

for i in range(0,N):
    soma = 0

    X,Y = map(int,input('').split())

    if X < Y:
        for j in range(X+1,Y):
            if j % 2 == 1:
                soma += j
    elif X > Y:
        for j in range(Y+1,X):
            if j % 2 == 1:
                soma += j
    
    print(soma)