#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'a largura vale {l} m², o comprimento vale {c}m², e área deste terreno vale {a:.2f}m²')

l=float(input('digite a largura do terreno:'))
c=float(input('digite o comprimento do terreno:'))
area(l,c)
