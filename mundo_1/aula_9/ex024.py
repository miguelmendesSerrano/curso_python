# Verificando as primeiras letras de um texto
cidade = input('Digite o nome da sua cidade: ').strip()
check = cidade.upper().split()
print('Sua cidade começa com "Santo"?\n{}'.format('SANTO' in check[0]))
# outra abordagem
print(cidade[:5].upper() == 'SANTO')
