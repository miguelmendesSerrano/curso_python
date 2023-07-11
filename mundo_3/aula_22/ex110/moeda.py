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


def resumo(valor=0, taxa=10, taxar=5):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Com {taxa}% de aumento: {aumentar(valor,taxa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(valor,taxar, True)}')
    print('=' * 30)

