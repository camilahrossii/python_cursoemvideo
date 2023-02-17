# Faça um ṕrograma que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A quantidade de vezes que a letra "A" aparece é {}.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A')+1))
