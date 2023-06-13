# Cadastro de Trabalhador em Python
from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = date.today().year - int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (35 - (date.today().year - cadastro['contratação'])) + cadastro['idade']
print('=======< DADOS >=======')
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
