# Este programa faz sorte de amigo secreto

import random
pessoas = ['João','Ana','Carlos','Marcia']

# Definindo a função sorteio

def sorteio(pessoas):
    amigos = pessoas.copy()
    #random.shuffle(amigos)

    embaralhar = True
    contador = 0
    while embaralhar == True:
        random.shuffle(amigos)
        embaralhar = False
        contador += 1
    
        for i in range(0,len(pessoas)):
            if amigos[i] == pessoas[i]:
                embaralhar = True
    
    print('O programa embaralhou', contador, 'vezes')
    return amigos

amigos = sorteio(pessoas)

print (pessoas)

print (amigos)


