"""
Arborilda é uma jovem dona de uma loja de jogos de mesa 
que tem crescido bastante nos últimos meses. Até então, 
Arborilda tem se organizado usando papel e lápis, mas é 
cada vez mais difícil executar as manipulações necessárias 
nas requisições de produtos com o crescente número de clientes a importunando.

Conhecendo sua reputação e seu conhecimento em Python, 
Arborilda pede a sua ajuda para ajudá-la a se organizar melhor.

A primeira coisa que Arborilda faz ao chegar ao trabalho de 
manhã cedo, é reler todas as requisições de produtos, da mais recente para a mais antiga.
"""
n = int(input())
pedidos = []
for i in range(n):
    pedidos.append(input())
for i in range(0,len(pedidos)-1):
    print(''+pedidos[-1],end=', ')
    pedidos.pop()
if len(pedidos)>0:
    print(pedidos[0])