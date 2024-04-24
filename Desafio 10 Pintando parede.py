# DESAFIO 10 - Faça um programa que leia a largura e altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta nescessária para pinta - lá.
# Sabendo que cada litro de tinta pinta uma área de 2 m2.

print('Desafio 10 iniciando.')
l = float(input('Qual a largura de sua parede?'))
a = float(input('Qual a altura de sua parede?'))
ap = (l * a)
lt = (ap / 2)
print(f'Para um área de {ap} metros. Será nescessário: {lt} Lts de tinta.')
print('>>> FIM <<<')

# Obs: Se fosse calcular mais de uma parede, a variavel AP seria = (l * a) * qtd de paredes.








