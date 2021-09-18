# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.


def conversao_hora():
    while True:
        hrs = str(input('digite o número de horas:'))
        while not hrs.isnumeric():
                print('digite um número para validar o horário!')
                hrs=str(input('digite o número de horas:'))
        hrs=int(hrs)
        while hrs>24 :
            print('digitou errado!')
            hrs = int(input('digite novamente o  número de horas:'))
        min = str(input('digite o número de minutos:'))
        while not min.isnumeric():
            print('digite um número para validar o horário!')
            min = str(input('digite o número de minutos:'))
        min=int(min)
        while min>60:
            print('digitou errado!')
            min = int(input('digite novamente o  número de minutos:'))
        if min==60:
            hrs=hrs+1
            min=0
        if hrs>12:
            if hrs==24:
                print(f'00:{min} PM')
            else:
                print(f'{hrs-12}:{min} PM')

        elif hrs<=12:
            print(f'{hrs}:{min} AM')
        escolha = str(input('você quer continuar?[S]im ou [N]ao:')).strip().upper()[0]
        if escolha=='N':
            print('encerrando o programa...')
            break



conversao_hora()


