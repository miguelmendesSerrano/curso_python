# Aumentos múltiplos
salario = float(input('Qual o salário atual? R$'))
if salario <= 1250:
    print('O novo salario com aumento de 15 % será: R${:.2f}'.format(salario + (salario * 15/100)))
else:
    print('O novo salário com aumento de 10 % será de: R${:.2f}'.format(salario + (salario * 10/100)))
