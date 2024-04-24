from math import trunc

print('Iniciando desafio 03 Quebrando Números.')
nome = str(input('Olá! Qual é o seu nome:'))
print(f'Legal! Prazer em te conhecer {nome}.')
num = float(input('Digite um número com virgulas:'))
part_int = trunc(num)
print(f'O número escolhido foi {num}. E a sua porção inteira é {part_int}')
