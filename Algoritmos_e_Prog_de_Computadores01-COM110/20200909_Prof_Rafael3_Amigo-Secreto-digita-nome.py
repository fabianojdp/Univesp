import time

pessoas = ['João','Ana','Carlos','Marcia']
amigos = ['Ana', 'Carlos','Marcia','João']

print(pessoas)

print(amigos)

def verifica_amigo(pessoas,amigos):
    sair = False
    while sair == False:
        print('Lista pessoas:\n',pessoas,'\n')
        usuario = input('Digite s para sair ou digite seu nome: ')
        if usuario in pessoas:
            i = pessoas.index(usuario)
            print('Seu amigo secreto é', amigos[i])
            time.sleep(3)
            print('\n'*25)
        elif usuario == 's':
            sair = True
            del amigos
            print('\nPrograma finalizado!')
        else:
            print('Entrada inválida!\n')

print('\n')

verifica_amigo(pessoas,amigos)
    
