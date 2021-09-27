# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def desenha_retangulo(lin,col):
    if lin>20:
        lin=20
    if col>20:
        col=20
    print('+',end='')
    for c in range(0,lin):
        print('−−',end='')
    print('+')
    for l in range(0,col):
        print('|',end='')
        print(' '*lin*2,end='')
        print('|')
    print('+',end='')
    for c in range(0,lin):
        print('−−',end='')
    print('+')


lin=int(input('digite o número de linhas:'))
col=int(input('digite o número de colunas:'))

desenha_retangulo(lin,col)
