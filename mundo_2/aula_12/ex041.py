# Classificando Atletas
from datetime import date
atual = date.today().year
nasc = int(input('Qual ano você nasceu? '))
idade = atual - nasc
if idade <= 9:
    print('{} anos. Sua classificação é: \033[36mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('{} anos. Sua classificação é: \033[33mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print('{} anos. Sua classificação é: \033[32mJÚNIOR\033[m'.format(idade))
elif idade <= 25:
    print('{} anos. Sua classificação é: \033[34mSÊNIOR\033[m'.format(idade))
else:
    print('{} anos. Sua classificação é: \033[31mMASTER\033[m'.format(idade))
