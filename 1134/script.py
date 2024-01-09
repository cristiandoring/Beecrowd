verificador = codigo = gasolina = alcool = diesel = 0

while verificador == 0:
    if codigo == 4:
        break
    
    if verificador == 0:
        codigo = int(input(''))

        if codigo < 0 and codigo > 4:
            verificador = 1

        else:
            if codigo == 1:
                alcool += 1
            elif codigo == 2:
                gasolina += 1
            elif codigo == 3:
                diesel += 1

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
 