# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
#     a) de 1 até 10, de 1 em 1                                                                                                                                              
#     b) de 10 até 0, de 2 em 2                                                                                                                                            
#     c) uma contagem personalizada

from time import sleep


def contador(ini, final, passo):
    if passo < 0:
        passo=abs(passo)

    elif passo==0:
        passo=1

    if ini>final:
        print(f'\na contagem do {ini} até o {final},de {passo} em {passo}')
        for num in range(ini, final - 1, -passo):
            # sleep(0.37)
            print(num, end=' ')

    else:

        print(f'a contagem do {ini} até o {final}, de {passo} em {passo}:')
        for num in range(ini, final + 1, passo):
            # sleep(0.37)
            print(num, end=' ')


contador(1, 10, 1)
contador(10, 0, -2)
print('agora é sua vez!')
ini = int(input('digite o valor inicial:'))
final = int(input('digite o valor final:'))
passo = int(input('digite o valor do passo:'))
contador(ini, final, passo)

