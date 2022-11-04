#conversor de moeda
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.65
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
print('-' *12)
##produto com desconto
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
