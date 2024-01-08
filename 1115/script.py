def mostrar_quadrante(x,y):
    if x > 0:
        if y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if y > 0:
            print('segundo')
        else:
            print('terceiro')

while True:
    x,y = map(int,input('').split())

    if x == 0 or y == 0:
        break
    else:
        mostrar_quadrante(x,y)


