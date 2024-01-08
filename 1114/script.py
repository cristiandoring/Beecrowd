senha = 2002

while True:
    senha_digitada = int(input(''))
    
    if senha_digitada == senha:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')