#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
 def soma_3_arg(n1,n2,n3):
    s=n1+n2+n3
    return print(f'a soma vale {s}')


soma_3_arg(2,3,4213)

#Faça um programa, com uma função que necessite de um argumento.
#A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

 def sinal(arg):
    if arg>0:
        return print('Positivo')
    elif arg==0:
        return print("Nulo")
    else:
        print('negativo')


arg=float(input('digite um número:'))
sinal(arg)
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaimposto(imposto,custo):
    imposto=imposto/100
    venda=custo*(1+imposto)
    return print(f'o valor para venda do produto(com imposto) adicionado é de R${venda}')


imposto=int(input('digite o valor da taxa de imposto:'))
custo=int(input('digite o valor do custo do produto:'))
somaimposto(imposto,custo)



