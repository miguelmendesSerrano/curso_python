# Aquele clássico da Média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:  '))
media = (n1 + n2) / 2
if media < 5:
    print('Média {:.1f} \033[31mREPROVADO.\033[m'.format(media))
elif 7 > media >= 5:
    print('Média {:.1f} \033[33mRECUPERAÇÃO.\033[m'.format(media))
else:
    print('Média {:.1f} \033[32mAPROVADO.\033[m'.format(media))
