#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.



def maior(*num):
    maior=0
    print('=-'*30)
    print('os numeros são:',end=' ')
    for v in num:
        print(v,end=' ')
    print('e o maior entre eles é ',end=' ')
    for c in range(0,len(num)):
        if c==0:
            maior=num[0]
        else:
            if maior<num[c]:
                maior=num[c]

    print(maior)
    print('=-'*30)
maior(2,11,9)
maior(930,2,929)
maior(9,2,23,340,9,71,7)
