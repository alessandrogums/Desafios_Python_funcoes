#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def LeiaInt(num):
    correto = False
    valor = 0
    while correto==False:
        valor=str(num)
        if num.isnumeric():
            valor = int(num)
            print(f'o número digitado é {valor}')
            correto = True
            if correto:
                return
        else:
            print('erro!!DIGITE UM NUMERO')
            num = input('digite um número:')

num=input('digite um número:')
LeiaInt(num)
