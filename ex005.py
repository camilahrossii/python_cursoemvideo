cont = input('Digite algo:')

print('O tipo primitivo desse valor é: ' ,type(cont))
print('É numérico?' ,cont.isnumeric())
print('Está em letras minúsculas? ' ,cont.islower())
print('Está em letras maiúsculas? ' ,cont.isupper())
print('Só tem espaços? ',cont.isspace())
print('Só tem letras? ',cont.isalpha())
print('Tem letras e números? ',cont.isalnum())
print('Está capitalizada? ' ,cont.istitle())

