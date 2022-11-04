##verificando as primeiras letras de um texto
cid = str(input('Em qual cidade você naceu?')).strip()
print(cid[:5].upper() == 'SANTO')
##procurando uma string dentro de outra
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
##primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))