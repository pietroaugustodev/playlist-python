print('Calculadora')

print('Escolha qual operação deseja fazer: *, +, - ou /')

operador = input()
num1 = input('Informe o primeiro número para fazer o cálculo: ')
num2 = input('Informe o segundo número para fazer o cálculo: ')

if operador == '+':
    print('\nResultado:', float(num1) + float(num2))

elif operador == '*':
    print('\nResultado:', float(num1)* float(num2))

elif operador == '-':
    print('\nResultado:', float(num1) - float(num2))

elif operador == '/':
    print('\nResultado:', float(num1) / float(num2))
    