# Índice de Massa Corporal
peso = float(input('Qual o seu peso? (kg)  '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / altura**2
print('IMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[33mAbaixo do Peso\033[m')
elif 18.5 <= imc < 25:
    print('\033[34mPeso Ideal\033[m')
elif 25 <= imc < 30:
    print('\033[33mSobrepeso\033[m')
elif 30 <= imc < 40:
    print('\033[33mObesidade\033[m')
else:
    print('\033[31mObesidade Mórbida\033[m')
