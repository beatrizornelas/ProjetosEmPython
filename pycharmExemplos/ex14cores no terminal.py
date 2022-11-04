#\033[style, text, back   m
# style: 0 none, 1 bold, 4 underline(sublinhado), 7 negative(fundo branco, letra preta)
# text: 30 branco,31 vermelho,32 verde,33 amarelo,34 azul,35 roxo,36 azul claro,37 cinza
# back: cores de fundo, msm sequência que acima só que do 40 ao 47
print('\033[0;30;41mOLá, Mundo!\033[m')
print('\033[4;33;44mOlá, Mundo!\033[m')
print('\033[1;35;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
#exemplo
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
