#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

 import datetime
ano_atual=datetime.datetime.now().year

def voto(ano_nascimento):
    idade=ano_atual-ano_nascimento
    if idade < 16:
        return print(f'você não pode votar,pois tem {idade} anos!')
    elif 60>idade>16:
        return print('seu voto é obrigatório!')
    else:
        return print('seu voto é opcional!')



ano_nascimento=int(input('digite seu ano de nascimento:'))
voto(ano_nascimento)
