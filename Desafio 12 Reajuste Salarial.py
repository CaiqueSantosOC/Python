# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.
# Com 15% de aumento.

print('Parabéns! Trago boas noticias! Você recebeu um aumento de 15% em seu salário!')
salario_atual = float(input('Qual o valor de seu salário atualmente?'))
aumento = salario_atual * 15 / 100
salario_novo = salario_atual + aumento
print(f'Parabéns! Você recebeu um aumento no valor de R${aumento:.2f} \nLogo seu salário passou de R${salario_atual:.2f}, para o valor de R${salario_novo:.2f}')
print('>>> FIM <<<')
