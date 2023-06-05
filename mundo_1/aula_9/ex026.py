# Primeira e última ocorrência de uma string
frase = input('Digite uma frase para analise: ').strip()
print('A letra "A" aparece: {} vezes.'.format(frase.upper().count('A')))
print('Aparece pela primeira vez na posição: {}'.format(frase.upper().find('A')+1))
print('Aparece pela última vez na posição: {}'.format(frase.upper().rfind('A')+1))
