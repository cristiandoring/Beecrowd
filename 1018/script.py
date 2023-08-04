N = int(input(''))

cem = N//100
cinquenta = ((N//50) - cem*1)
vinte = (N//20 - cem - cinquenta)-cem-(cinquenta*1/2)
dez = N//10 - (cem*100 + cinquenta*50 + vinte*20)
cinco = N//5 -(cem*100 + cinquenta*50 + vinte*20 + dez*10)
dois = N//2 - (cem*100 + cinquenta*50 + vinte*20 + dez*10 + cinco*5)
um = N - (cem*100 + cinquenta*50 + vinte*20 + dez*10 + cinco*5 + dois*2)

print(N)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')