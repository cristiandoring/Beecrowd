salario = float(input(''))

if salario >= 0 and salario <=2000:
    print('Isento')
elif salario > 2000 and salario <= 3000:
    print(f'R$ {(salario - 2000)*0.08:.2f}')
elif salario > 3000 and salario <= 4500:
    print(f'R$ {(1000)*0.08 + (salario-3000)*0.18:.2f}')
elif salario > 4500:
    print(f'R$ {(1000)*0.08 + (1500)*0.18 + (salario-4500)*0.28:.2f}')