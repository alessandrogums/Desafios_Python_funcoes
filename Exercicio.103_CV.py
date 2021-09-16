#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

 def ficha(nome='', gols=''):
    if nome in '':
        nome = '<desconhecido>'
    if gols in '' or gols not in '1234567890':
        gols = 0
    else:
        gols = int(gols)
    return print(f'o jogador {nome} fez {gols} gols')


nome = str(input('digite o nome do jogador:')).strip()
gols = str(input('digite o número de gols:')).strip()

ficha(nome,gols)
