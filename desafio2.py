# Crie um algoritmo que leia um numero e mostre o seu dobro e triplo e raíz quadrada;
n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = n**(1/2)
# pow(n,(1/2)
print('O dobro de {} é {}; \nO triplo é {}; \nA raíz quadrada é {:.2f}!'.format(n,d,t,rq))