a,b,c = map(float,input('').split())

#ordena em ordem decrescente
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

if a >= b+c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > (b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < (b**2 + c**2):
        print('TRIANGULO ACUTANGULO')

    if a == b and a == c:
        print('TRIANGULO EQUILATERO') 
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
