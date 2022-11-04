''' Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, do zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'desesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        continuar = str(input(f'Você digitou o número {cont[núm]}. Você quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'N':
            break
    else:
        print('Você digitou um número inválido. Tente novamente.')
print('Obrigado pela participação!')
print( '_' * 40)
print("\n")


'''exercício: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense. '''
from time import sleep
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino','Athletico-PR', 'Internacional', 'Fluminense',
         'Atlético-GO', 'Cuiabá', 'Ceará', 'São Paulo', 'América-MG', 'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print('Informações sobre os times do Brasileirão')
while True:
    print("\n")
    print('=-' * 15 + 'INICIO' + '=-' * 15)

    escolha = int(input('''Escolha entre as opções: 
    [ 1 ] para os 5 primeiros classificados
    [ 2 ] para os 4 últimos classificados
    [ 3 ] para todos os classificados em ordem alfabética
    [ 4 ] para a classificação de algum dos times
     ---->  '''))
    print('\n')
    print("=-" * 40)
    if escolha == 1:
        print(f'Os 5 primeiro classificados no Brasileirão são:')
        for t in times[:5]:
            print(f'{times.index(t)+1}º', t)
    elif escolha == 2:
        print(f'Os 4 últimos classificados no Brasileirão são:')
        for f in times[-4:]:
            print(f'{times.index(f)+1}º', f)
    elif escolha == 3:
        print(f'Os 20 classificados do Brasileirão em ordem alfabética são:')
        for t in sorted(times):
            print(t)
    elif escolha == 4:
        nome = str(input('De qual time você quer saber? ')).strip().capitalize()
        if nome in times:
            print(f'O time {nome} está em {times.index(nome) + 1}º na tabela.')
        else:
            print(f'O {nome} não está classificado para o brasileirão.')
    print('-' * 40)
    resp = int(input('''Quer escolher entre as opções novamente?
    (1) sim      (2) não       -->  '''))
    print('\n')
    if resp == 2:
        break
print("=-" * 40)
print('OBRIGADO POR USAR O PROGRAMA! ATÉ BREVE :)')
print("=-" * 40)