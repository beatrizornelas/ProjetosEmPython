##salário com 15% de aumento
salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com o aumento, passa a receber R${:.2f}'.format(salário, novo))
print('---------------------------')
##Carro alugado, preço a pagar por km rodado (R$60 por dia e R$0,15 por KM rodado
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
print('-------------------------')
