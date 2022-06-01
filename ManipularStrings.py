#Manipulando Cadeia de textos ou cadeia de caracteres ou strings
#texto='Curso em Vídeo Python' #O python cria mini espaços e cada um desse espaço recebe uma string
   #CURSO
   #01234

#Fatiamento - Consegui pegar pedaços da String
# frase=[9]  ele vai identificar qual string está na posição 9
# frase=[9:13] ele vai pegar todas as letras que estão na posição que vai de 0 a 13,
# porém ele remove a última posição 12

# frase=[9:21:2]- Vai pegar todas as letras de 9 a 21.. e vai e ignorando a cada duas posições
# frase=[:5] - ele vai começar do início e vai até a posição 5
# frase=[15:] - ele vai começar da posição 15 até o final
# frase=[9::3] - começa na posição 9 e vai até o final, porém vai pulando a cada 3 posições

#Análise de String por meio de funções:
# len(frase) - conta a quantidade total de caracteres utilizada para escrever a frase
# frase.count('o') - Vai me contar quantas vezes tem a letra o
# frase.coutn('o', 0, 13) - Ele vai me imprimir quantos os tem da posição 0 a posição 13
# frase.find('deo') - Ele vai indicar em qual posição começou a frase deo
# frase.find('Android') - Ele retorna posição -1, ou seja retorna que não tem essa string na posição
#'Curso' in frase - vai retornar True verdadeiro (estamos utilizando um operador)


#Transformação - Mexemos na string através de metodos(POO)
#ffrase = str(input('Digite a sua frase: '))
# frase.replace ('Python', 'Android') - ele substitui a palavra python por Android
# frase.upper() - ele converte todas as letras em maiúscula
# frase.lower() - Ele converte tudo em letra minúscula
# frase.capitalize() - Deixa apenas a primeira letra da Frase como maiúscula
# frase.strip() - Remove espaços do início e fim
# frase.rstrip() - Remove os espaços da direita right - eu posso usar o r em outras funções
# frase.lstrip() - Remove os espaços da esquerda strip - eu posso usar o l em outras funções
# frase.title() - Analisa quantas palavras tem deixa a primeira letra das palavras em maiuscula


#Divisão de strings
# frase.split() - Gera um lista com cada palavra em uma cadeia


#Junção
# '-'.join(frase) junta as frases e coloca o - exemplo curso-em-video

# Se usar uma função de transformação de string, eu consigo alterar uma string


# print('''para escrever textos enormes''') usar 3 aspas '  ou "
frase = 'Curso em vídeo Python'
print(len(frase.strip()))
print(frase.replace('Python','Android'))
frase = frase.replace('Python','Android')
print('frase {}'.format(frase))
print('Curso' in frase)
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[0])
