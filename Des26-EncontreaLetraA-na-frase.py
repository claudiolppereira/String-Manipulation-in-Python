frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantos As aparecem? {}'.format(frase.count('A')))
print('O primeiro A aparece na posição {}'.format(frase.find('A')+1))
print('O último A aparece na posição {}'.format(frase.rfind('A')+1))