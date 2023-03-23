"""
André adora brincar com seus amiguinhos usando a língua do "p", mas nem sempre eles conseguem 
reproduzir com tanta maestria as frases trocando todas as consoantes por "p". 

Para ajudar André a não perder mais tempo explicando para os seus coleguinhas como 
é a pronúncia correta dessa linguagem, você decidiu escrever um programa que processa uma 
frase e retorna ela traduzida."""
consoantes = 'bcdfghjklmnpqrstvwxyz'
string = input()
nova_string = []
for i in list(string):
    if i.lower() in list(consoantes):
        nova_string.append('p')
    else:
        nova_string.append(i)
print(''.join(nova_string))