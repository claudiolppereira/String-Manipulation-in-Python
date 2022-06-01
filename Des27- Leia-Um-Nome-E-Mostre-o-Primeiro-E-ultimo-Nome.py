n = str(input('Digite o nome completo: '))
n = n.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))