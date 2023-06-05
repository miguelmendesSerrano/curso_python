# Radar Eletronico
vel = float(input('Qual a velocidade atual: '))
if vel > 80:
    print('Você ultrapassou o limite, será multado em R${:.2f}'.format((vel - 80) * 7))
print('Tenha um bom dia.')
