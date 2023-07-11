def aumentar(valor, taxa):
    preço = valor + (valor * taxa / 100)
    return preço


def diminuir(valor, taxa):
    preço = valor - (valor * taxa / 100)
    return preço


def dobro(valor):
    preço = valor * 2
    return preço


def metade(valor):
    preço = valor / 2
    return preço

