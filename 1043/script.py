a,b,c = map(float,input('').split())

if a >= b+c or b >= a+c or c >= a+c:
    print(f'Area = {((a + b)/2)*c:.1f}')
else:
    print(f'Perimetro = {a + b + c:.1f}')