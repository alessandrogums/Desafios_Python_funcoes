#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show):
    fator = 1
    print(f'{num}! =',end=' ')
    if not show:

        while num != 1:
            fator *= num
            num -= 1
        return print(fator,end=' ')
    else:

        for c in range(num,0,-1):
            fator*=c
            if c==1:
                return print(f'1= {fator}')
            print(f'{c}',end='x ')




num=int(input('digite um número:'))
fatorial(num,show=True)
