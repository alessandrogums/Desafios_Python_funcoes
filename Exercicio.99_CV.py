
#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


from random import randint


def sorteia(list):
    for c in range(1, 6):
        num = randint(0, 100)
        lista_numeros.append(num)
    print(f'os números sorteados foram:{lista_numeros}')


def somapar(list):
    soma = 0
    for v in list:
        if v % 2 == 0:
            soma += v

    print(f'A soma dos números pares desta lista deu {soma}')


lista_numeros = list()
sorteia(lista_numeros)
somapar(lista_numeros)
