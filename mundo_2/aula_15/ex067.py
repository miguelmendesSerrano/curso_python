# Tabuada v3.0
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    print('=' * 40)
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i:2}')
    print('=' * 40)
print('-' * 20)
print('Programa finalizado.')
