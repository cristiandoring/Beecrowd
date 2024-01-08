while True:
    X,Y = map(int,input('').split())

    if X == Y:
        break
    else:
        if X > Y:
            print('Decrescente')
        else:
            print('Crescente')        