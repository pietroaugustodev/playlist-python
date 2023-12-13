print('Programa dinâmico')

num = int(input('Informe um número positivo inteiro para fazer a potenciação dele com ele mesmo: '))

while num < 1:
    if num < -50:
        print('EU FALEI UM NÚMERO POSITIVO')
        break
    elif num < 0 and num > -50:
        num = int(input('Informe um número positivo: '))

    elif num == 0:
        break


if num > 0: 
    print(num**num)
