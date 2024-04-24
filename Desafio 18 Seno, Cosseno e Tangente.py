from math import cos, sin, tan, radians

print('Iniciando desafio 18 Pyhton')
angulo = float(input('Digite o valor do ângulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O valor do ÂNGULO foi {angulo}. E seus respectivos valores: \nSENO: {seno:.2f} \nCOSSENO: {cosseno:.2f} \nTANGENTE: {tangente :.2f}')

