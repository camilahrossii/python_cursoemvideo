
print('=-'*10)
print('CALCULADORA')
print('=-'*10)
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('Digite: + [soma], - [subtração], * [multiplicação] e / [divisão]')
op = input('Qual operação deseja executar? ')
if op == '+':
    op = num1 + num2
    print('O resultado é {}'.format(op))
elif op == '-':
    op = num1 - num2
    print('O resultado é {}'.format(op))
elif op == '*':
    op = num1 * num2
    print('O resultado é {}'.format(op))
elif op == '/':
    op = num1 / num2
    print('O resultado é {}'.format(op))
else:
    print('Operação inválida. Tente novamente.')