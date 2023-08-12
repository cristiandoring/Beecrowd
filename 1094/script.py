N = int(input(''))
total_cobaias = coelhos = ratos = sapos = 0
for i in range(0,N):
    quantidade, tipo = map(str,input('').split())
    cobaias = int(quantidade)

    total_cobaias += cobaias

    if tipo == 'C':
        coelhos += cobaias 
    elif tipo == 'S':
        sapos += cobaias
    elif tipo == 'R':
        ratos += cobaias
print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(coelhos/total_cobaias)*100:.2f} %')
print(f'Percentual de ratos: {(ratos/total_cobaias)*100:.2f} %')
print(f'Percentual de sapos: {(sapos/total_cobaias)*100:.2f} %')