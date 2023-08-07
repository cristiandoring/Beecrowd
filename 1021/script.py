
reais,centavos = map(float,input('').split('.'))

cem = reais//100
cinquenta = (reais - cem*100)//50
vinte = (reais - cem*100 - cinquenta*50)//20
dez = (reais - cem*100 - cinquenta*50 - vinte*20)//10
cinco = (reais - cem*100 - cinquenta*50 - vinte*20-dez*10)//5
dois = (reais - cem*100 - cinquenta*50 - vinte*20-dez*10-cinco*5)//2
um = (reais - cem*100 - cinquenta*50 - vinte*20 - dez*10 - cinco*5 - dois*2)//1

cinquenta_centavos = (centavos)//50

vinte_cinco_centavos = (centavos - cinquenta_centavos*50)//25
dez_centavos = (centavos - cinquenta_centavos*50-vinte_cinco_centavos*25)//10
cinco_centavos = (centavos - cinquenta_centavos*50-vinte_cinco_centavos*25-dez_centavos*10)//5
um_centavo = (centavos -cinquenta_centavos*50-vinte_cinco_centavos*25-dez_centavos*10-cinco_centavos*5)

print('NOTAS:')
print(f'{cem:.0f} nota(s) de R$ 100.00')
print(f'{cinquenta:.0f} nota(s) de R$ 50.00')
print(f'{vinte:.0f} nota(s) de R$ 20.00')
print(f'{dez:.0f} nota(s) de R$ 10.00')
print(f'{cinco:.0f} nota(s) de R$ 5.00')
print(f'{dois:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um:.0f} moeda(s) de R$ 1.00')
print(f'{cinquenta_centavos:.0f} moeda(s) de R$ 0.50')
print(f'{vinte_cinco_centavos:.0f} moeda(s) de R$ 0.25')
print(f'{dez_centavos:.0f} moeda(s) de R$ 0.10')
print(f'{cinco_centavos:.0f} moeda(s) de R$ 0.05')
print(f'{um_centavo:.0f} moeda(s) de R$ 0.01')

