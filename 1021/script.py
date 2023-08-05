
N = float(input(''))

cem = N//100
cinquenta = (N - cem*100)//50
vinte = (N - cem*100 - cinquenta*50)//20
dez = (N - cem*100 - cinquenta*50 - vinte*20)//10
cinco = (N - cem*100 - cinquenta*50 - vinte*20-dez*10)//5
dois = (N - cem*100 - cinquenta*50 - vinte*20-dez*10-cinco*5)//2
um = (N - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2)//1

cinquenta_centavos = (N - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2-um*1)//0.5

vinte_cinco_centavos = (N - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2-um*1-cinquenta_centavos*0.5)//0.25
dez_centavos = (N - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2-um*1-cinquenta_centavos*0.5-vinte_cinco_centavos*0.25)//0.1
cinco_centavos = (N - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2-um*1-cinquenta_centavos*0.5-vinte_cinco_centavos*0.25-dez_centavos*0.10)//0.05
um_centavo = (N - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2-um*1-cinquenta_centavos*0.5-vinte_cinco_centavos*0.25-dez_centavos*0.10-cinco_centavos*0.05)//0.01

cem = int(cem)
cinquenta = int(cinquenta)
vinte = int(vinte)
dez = int(dez)
cinco = int(cinco)
dois = int(dois)
um = int(um)
cinquenta_centavos = int(cinquenta_centavos)
vinte_cinco_centavos = int(vinte_cinco_centavos)
dez_centavos = int(dez_centavos)
cinco_centavos = int(cinco_centavos)
um_centavo = int(um_centavo)

print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinquenta} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{cinquenta_centavos} moeda(s) de R$ 0.50')
print(f'{vinte_cinco_centavos} moeda(s) de R$ 0.25')
print(f'{dez_centavos} moeda(s) de R$ 0.10')
print(f'{cinco_centavos} moeda(s) de R$ 0.05')
print(f'{um_centavo} moeda(s) de R$ 0.01')

