def media():
    print(f'media = {(n1+n2)/2:.2f}')

n1 = float(input())

while n1 < 0 or n1 > 10:
    print('nota invalida')

    n1 = float(input())

n2 = float(input())

while n2 < 0 or n2 > 10:
    print('nota invalida')

    n2 = float(input())

media()
    