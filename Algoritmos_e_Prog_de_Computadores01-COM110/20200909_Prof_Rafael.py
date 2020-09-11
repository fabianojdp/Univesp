# Este programa imprime uma lista de nomes

nomes = ['João','Ana','Carlos','Marcia']

c = len(nomes)

# Imprimindo nomes com o while
i = 0
while i < c:
    print(nomes[i])
    i += 1

# imprimindo nomes com o for
print('\n')

"""range(0,3)
t=range(0,3)
t[0]
0 """

for i in range(0,c):
    print(nomes[i])
    print(i) # índice

print('\n')

for i in nomes:
    print(i)
