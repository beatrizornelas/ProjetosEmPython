soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os valores solicitados é {} '.format(soma))
print ('='* 40)
# lendo um número inteiro e dizendo se é ou não um número primo
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[36m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')