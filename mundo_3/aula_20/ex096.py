# Função que calcula área
def area(largura, comprimento):
    a = largura * comprimento
    print(f"A área do terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f} m².")


print('=' * 20)
print('Controle de Terrenos')
print('=' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
