# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                               
# – A menor nota                                                                                                                                                              
# – A média da turma
# – A situação (opcional)


def notas(*numeros, situacao=False):
    total = len(numeros)
    dicionario = dict()
    dicionario['total'] = total
    maior = menor = 0
    for i, v in enumerate(numeros):
        if i == 0:
            dicionario['maior'] = v
            dicionario['menor'] = v
        elif v > dicionario['maior']:
            dicionario['maior'] = v
        elif dicionario['menor'] > v:
            dicionario['menor'] = v

    dicionario['media'] = (sum(numeros) / len(numeros))

    if situacao == True:
        if 9>dicionario['media'] > 7:
            dicionario['situacao'] = 'Regular'
        elif dicionario['media'] > 9:
            dicionario['situacao'] = 'Ótimo'
        else:
            dicionario['situacao'] = 'nada bom:('
    return dicionario


boletim = notas(8, 9,1, situacao=False)
print(boletim)
