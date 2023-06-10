# Maior e menor valores em Tupla
from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {n}\nO maior número foi: {max(n)}\nO menor foi: {min(n)}')
