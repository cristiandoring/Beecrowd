X=0
while True:
    verificador1 = verificador2 = 0

    while verificador1 == 0:
        nota1 = float(input())

        if nota1 >= 0 and nota1 <=10:
            verificador1 = 1
        else:
            print('nota invalida')

    while verificador2 == 0:
        nota2 = float(input())

        if nota2 >= 0 and nota2 <=10:
            verificador2 = 1
        else:
            print('nota invalida')

    print(f'media = {(nota1+nota2)/2:.2f}')

    verifica_novo_teste = 0

    while verifica_novo_teste == 0:
        print('novo calculo (1-sim 2-nao)')
        X = int(input())

        if X == 1 or X == 2:
            verifica_novo_teste = 1

    if X == 2:
        break
    else:
        continue


