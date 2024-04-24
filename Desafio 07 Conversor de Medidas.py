# DESAFIO 08 - Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros.

print('iniciando desafio em Python')
me = int(input('Digite o número para conversão:'))
print(f'Resultado da convers]ao de: {me} metros. em centimentros: {me * 100}. Milimetros: {me * 1000}.')

####### outra opção de solução ######
ce = me * 100
mi = me * 1000
print(f'Resultado da conversão de: {me} metros. \n Centimetros: {ce} \n Milimetros: {mi}')
