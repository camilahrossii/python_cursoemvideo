tot18 = totH = totM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade < 20 and sexo == 'F':
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de {tot18} maiores de 18 anos')
print(f'Total de {totH} homens cadastrados')
print(f'Total de {totM} mulheres com menos de 18 anos')