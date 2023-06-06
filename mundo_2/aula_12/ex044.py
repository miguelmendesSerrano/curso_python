# Gerenciador de Pagamentos
compra = float(input('Preços das compras: R$ '))
print('''Formas de Pagamento
[ 1 ] À vista dinheiro/pix
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção? '))
if opcao == 1:
    print('À vista dinheiro/pix desconto 10% total a pagar: R$ {:.2f}'.format(compra - (compra * 10/100)))
elif opcao == 2:
    print('À vista cartão desconto 5% total a pagar: R$ {:.2f}'.format(compra - (compra * 5/100)))
elif opcao == 3:
    print('2x no cartão, duas parcelas de R$ {:.2f}'.format(compra/2))
elif opcao == 4:
    parcelas = int(input('Em quantas vezes quer dividir? '))
    compra_juros = compra + (compra * 20/100)
    print('{}x no cartão, acrescimo de 20% de juros, {} parcelas de R$ {:.2f} total a pagar: R$ {:.2f}'.format(parcelas, parcelas, compra_juros/parcelas, compra_juros))
else:
    print('Opção inválida')
