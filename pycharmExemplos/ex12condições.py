tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
## Outro exemplo
print('x' * 80)
from random import randint
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
print('x' * 80)
# Outro exemplo
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! você excedeu a velocidade permitida.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa no valor de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
print('x' * 80)
# Outro exemplo
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))
print('x' * 80)
# Outro exemplo (desenvolva um programa q pergunta a distância
# de uma viagem em km.Calcule o preço da passagem, cobrando R$0,50
# por km para viagens de até 200km e R$0,45 para viagens mais longas)
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
print('x' * 80)
# Outro exemplo (Faça um programa que leia três números e mosre qual
# é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
