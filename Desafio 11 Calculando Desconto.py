# Faça um algoritmo que leia o preço de um produto.
# E mostre seu novo preço com 5% de desconto.

print('Iniciando desafio 11 aula de Python.')
print('Bem vindo a loja do Kaká. \n Todos nosso produtos estão com 5% de desconto.')
nome = input('Qual é o seu nome?')
print(f'É um prazer {nome}. Vamos ao desconto.')
produto = float(input('Qual o valor do produto escolhido R$?'))
desconto = (produto * 5 / 100)
valor_final = (produto - desconto)
print(f'Muito obrigado por comprar em nossa loja {nome}. \nO valor do seu produto com desconto é R$: {valor_final :.2f}')
print('VOLTE SEMPRE!!!.')
