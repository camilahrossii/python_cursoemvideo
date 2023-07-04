def aumentar(preço = 0, taxa = 0, formato = False):
    """
    Acrescenta uma taxa ao produto, soma o valor do produto + a taxa informada
    :param preço: preço do produto
    :param taxa: taxa percentual que será somada
    :param formato: se True vai aparecer formatada na tela, se False não terá formatação
    :return: se o formato estiver True o retorno vai ser com a função moeda que contém a formatação R$
    """
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato = False):
    """
    Subtrai taxa informada sobre o preço do produto
    :param preço: preço do produto
    :param taxa: taxa percentual que será subtraida
    :param formato: se True vai aparecer formatada na tela, se False não terá formatação
    :return: se o formato estiver True o retorno vai ser com a função moeda que contém a formatação R$
    """
    res = preço - (preço * taxa / 100)
    return res if not formato else moeda(res)

def dobro(preço = 0, formato = False):
    """
    Dobra o preço do produto
    :param preço: preço do produto
    :param formato:  se True vai aparecer formatada na tela, se False não terá formatação
    :return: se o formato estiver True o retorno vai ser com a função moeda que contém a formatação R$
    """
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato = False):
    """
    Reduz o preço do produto pela metade
    :param preço: preço do produto
    :param formato: se True vai aparecer formatada na tela, se False não terá formatação
    :return: se o formato estiver True o retorno vai ser com a função moeda que contém a formatação R$
    """
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    """
    Formatação R$ com 2 casa decimais
    :param preço: preço do produto
    :param moeda: formataçao R$
    :return: formatação R$ 00,00 trocando o '.' por ',' com 'replace()'
    """
    return f'{moeda}{preço:>6.2f}'.replace('.',',')

