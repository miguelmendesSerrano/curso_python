# Aprovando Empréstimo
valor_imovel = float(input('Qual o valor do imóvel? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))
parcela = valor_imovel / (anos * 12)
salario = float(input('Qual é o seu salário? R$ '))
# checando condiçoes para aprovar ou não o emprestimo
if parcela > (salario * 30/100):
    print('\n\033[31mEmpréstimo Negado!\033[m\nO valor da parcela é maior que 30% do seu salário.')
else:
    print('\n\033[32mEmpréstimo Aprovado!\033[m')
# imprimindo dados do emprestimo
print('\nValor do imóvel: \033[34mR$ {:.2f}\033[m\nNúmero de parcelas: {} vezes\nValor das parcelas: \033[33mR$ {:.2f}\033[m'.format(valor_imovel, (anos * 12), parcela))
