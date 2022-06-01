nome = str(input('Digite o nome completo: ').strip())
print('Nome com todas as letras maiusculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Total de Letras: {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras: '.format(nome.find(' '))) #Mostra quantas letras tem o primeiro nome
separador = nome.split() #Separa cada palavra em uma cadeia
print(separador)
print('Seu primeiro nome tem {}'.format(len(separador[0]))) #mosta quantidade de letras da primeira posição 0
print('Seu primeiro nome é: {}'.format(separador[0])) #mostra a palavra da primeira posição