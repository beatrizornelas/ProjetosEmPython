n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {} e {} é igual a {}'.format(n1, n2, média))
if média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif média <= 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
