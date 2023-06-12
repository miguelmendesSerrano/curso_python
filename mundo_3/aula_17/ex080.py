# Lista ordenada sem repetições
valores = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v >= valores[-1]:
        valores.append(v)
        print('Valor adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(valores):
            if v <= valores[posicao]:
                valores.insert(posicao, v)
                print(f'Valor adicionado na posição {posicao} da lista')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram {valores}')
