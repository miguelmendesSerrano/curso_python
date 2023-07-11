def aumentar(valor=0, taxa=0):
    preço = valor + (valor * taxa / 100)
    return preço


def diminuir(valor=0, taxa=0):
    preço = valor - (valor * taxa / 100)
    return preço


def dobro(valor=0):
    preço = valor * 2
    return preço


def metade(valor=0):
    preço = valor / 2
    return preço


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>6.2f}'.replace('.', ',')

