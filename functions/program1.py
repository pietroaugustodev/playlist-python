print('Programa para calcular a média')


def calcularMedia(num1, num2, num3):
    return (num1 + num2 + num3) / 3 


num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

MEDIA = round(calcularMedia(num1, num2, num3), 2)
MEDIA = 0.0

print('Sua média foi', MEDIA)


