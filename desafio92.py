from datetime import datetime
carteira = {}
carteira['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
carteira['idade'] = datetime.now().year - nasc
carteira['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if carteira['carteira'] != 0:
    carteira['contratação'] = int(input('Ano de Contratação: '))
    carteira['salário'] = float(input('Salário: R$'))
    carteira['aposentadoria'] = carteira['idade'] + ((carteira['contratação'] + 35) - datetime.now().year)
for k, v in carteira.items():
    print(f'    - {k} tem o valor {v}')