quantidade_grenais = vitorias_gremio = vitorias_inter = empates = 0

while True:
    gols_inter, gols_gremio = map(int,input().split())
    
    quantidade_grenais += 1

    if gols_gremio > gols_inter:
        vitorias_gremio += 1
    elif gols_inter > gols_gremio:
        vitorias_inter += 1
    else:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')

    novo_placar = int(input())

    if novo_placar == 2:
        break
        
    elif novo_placar == 1:
        continue
    else:
        print('entrada invalida')
        
        break
    
print(f'{quantidade_grenais} grenais')
print(f'Inter:{vitorias_inter}')
print(f'Gremio:{vitorias_gremio}')
print(f'Empates:{empates}')

if vitorias_gremio > vitorias_inter:
    print('Gremio venceu mais')
elif vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
else:
    print('Não houve vencedor')