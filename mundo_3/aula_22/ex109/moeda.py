def aumentar(valor=0, taxa=0, formato=False):
    preço = valor + (valor * taxa / 100)
    return preço if not formato else moeda(preço)


def diminuir(valor=0, taxa=0, formato=False):
    preço = valor - (valor * taxa / 100)
    return preço if not formato else moeda(preço)


def dobro(valor=0, formato=False):
    preço = valor * 2
    return preço if not formato else moeda(preço)


def metade(valor=0, formato=False):
    preço = valor / 2
    return preço if not formato else moeda(preço)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>6.2f}'.replace('.', ',')

