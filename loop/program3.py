import random

print('Programa para descobrir o número')

numSorteado = random.randint(0, 100)
tentativa = -1
tentativas = 0

while tentativa != numSorteado and tentativas != 10: 
    tentativa = int(input('Insera número: '))
    if tentativa != numSorteado and tentativa < numSorteado:
        print('Tente um número maior!')
    elif tentativa != numSorteado and tentativa > numSorteado:
        print('Tente um número menor!')
    tentativas += 1

if tentativas == 10 and tentativa != numSorteado:
    print('Perdeu! o número era', numSorteado)

else:
    print('Ganhou! o número era', numSorteado)
