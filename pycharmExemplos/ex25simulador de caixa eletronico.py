'''Simulador de caixa eletrônico, no qual pergunta o valor sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues
considerando que o caixa possui cédulas de: 1, 10, 20 e 50 '''
print('\033[0:30:41m =================== \033[m')
print('{:30}'.format('    BANCO CENTRAL'))
print('\033[0:30:41m =================== \033[m')
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('\033[0:31m ~~~~~~~~~~~~~~~~~~ \033[m')
print('    Volte sempre!')
print('\033[0:31m ~~~~~~~~~~~~~~~~~~ \033[m')