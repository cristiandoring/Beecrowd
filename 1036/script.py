A, B, C = map(float,input('').split())

delta = (B**2 - 4*A*C)

if delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(-B+(delta**(1/2)))/(2*A):.5f}')
    print(f'R2 = {(-B-(delta**(1/2)))/(2*A):.5f}')