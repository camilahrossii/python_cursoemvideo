def escreva(txt):
    tam = len(txt) + 5
    print('~' * tam)
    print(f'    {txt}')
    print('~' * tam)


msg = str(input('Escreva sua mensagem: '))
escreva(msg)