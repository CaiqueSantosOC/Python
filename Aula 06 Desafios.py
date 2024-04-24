import time

print('>>> DESAFIO AULA 06 PYTHON <<<')
time.sleep(1.5)
nome = input('Digite seu nome para iniciar seu desafio:')
time.sleep(1.5)
print(f'SEJA MUITO BEM VINDO AO SEU DESAFIO{nome}.')
time.sleep(1.5)
v = input('Digite alguma coisa:')
time.sleep(1.5)
print('Esse valor te'
      'm o tipo primitivo de:', type(v))
time.sleep(1.5)
print(f'{v}, È um número?', v.isnumeric())
time.sleep(1.5)
print(f'{v}, É alfabético?', v.isalpha())
time.sleep(1.5)
print(f'{v}, Está escrito com letras minúsculas?', v.islower())
time.sleep(1.5)
print(f'{v}, Está escrito com letras maiúsculas?', v.isupper())
time.sleep(1.5)
print(f'{v}, Pode ser impresso?', v.isprintable())
time.sleep(1.5)
print(f'{v}, É capitalizado?', v.istitle())
time.sleep(1.5)
print('>>> PARABÉNS!, VOCÊ CONCLUIU SEU DESAFIO. <<<')
print('>>> XAU OBRIGADO!!! <<<')


