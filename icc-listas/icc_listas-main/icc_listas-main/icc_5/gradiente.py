"""
Raphael está desenvolvendo um analisador de gradiente léxico para o seu 
mais novo experimento com Inteligência Artificial e processamento de texto 
em linguagem natural. Para isso, ele precisa saber, com precisão, se os 
caracteres de uma string são maiúsculos, minúsculos, espaços em branco ou dígitos numéricos.

Sabendo que você é um exímio programador, Raphael pediu sua ajuda nesta tarefa.
"""

n = input()
for i in list(n):  
    if i == ' ':
        print('W',end='')
    elif ord(i) >= 48 and ord(i) <= 57:
        print('D',end='')
    elif i.lower() == i:
        print('L',end='')
    elif i.upper() == i:
        print('U',end='')