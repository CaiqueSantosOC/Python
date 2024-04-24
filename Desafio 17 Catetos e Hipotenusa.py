from math import hypot

co = float(input('Qual o comprimento do cateto oposto:'))
ca = float(input('Qual o comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print(f'O resultado do valor da hipotenusa é {hi:.2f}')

#outra opção: hi= (co ** 2 + ca ** 2) ** (1/2) >> formula para hipotenusa.
