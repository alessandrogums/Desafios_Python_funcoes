# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

 def triangulo_numeros(n):
    cont=1
    colunas=0
    while n>=cont:
        colunas=0
        while cont >colunas:
            print(cont,end=' ')
            colunas+=1
        print()
        cont+=1


n=int(input('digite um número'))
triangulo_numeros(n)

# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.


def triangulo_numeros(n):
#     cont = 1
#     colunas = 0
#     v=1
#     while n >= cont:
#         colunas = 0
#         v=1
#         while cont > colunas:
#             print(v, end=' ')
#             v+=1
#             colunas += 1
#         print()
#         cont += 1

#
#
# n = int(input('digite um número'))
# triangulo_numeros(n)
