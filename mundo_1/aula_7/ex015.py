# Aluguel de Carros
dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
aluguel = dia * 60 + km * 0.15
print('O valor total a pagar é R${:.2f}'.format(aluguel))
