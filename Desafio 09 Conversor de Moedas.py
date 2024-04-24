# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:
# Considerando US$ 1.00 = R$ 5,07. (2023)

print('Iniciando desafio 10')
c = float(input('Digite o valor que está em sua carteira:'))
dolar = float(input('Qual o valor do dolar hoje?'))
d = 5.07
r = (c / d)
print(f'Com o saldo de R${c} em sua carteira.\nSerá possivel comprar US${r} dólares. \nJá que o dolar está {d} atualmente.')
