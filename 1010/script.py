peca1, quantidade_peca1, valor_unitario_peca1 = map(float,input('').split())
peca2, quantidade_peca2, valor_unitario_peca2 = map(float,input('').split())

peca1 = int(peca1)
quantidade_peca1 = int(quantidade_peca1)
peca2 = int(peca2)
quantidade_peca2 = int(quantidade_peca2)

print(f'VALOR A PAGAR: R$ {quantidade_peca1*valor_unitario_peca1+quantidade_peca2*valor_unitario_peca2:.2f}')