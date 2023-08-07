esqueleto = str(input(''))
grupo = str(input(''))
alimentacao = str(input(''))

if esqueleto == 'vertebrado':
    if grupo == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        elif alimentacao == 'onivoro':
            print('pomba')
    elif grupo == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        elif alimentacao == 'herbivoro':
            print('vaca')
elif esqueleto == 'invertebrado':
    if grupo == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
    elif grupo == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print('minhoca')