"""
Andreia e seu amigo, Brocado, estão jogando um jogo que eles mesmo inventaram, o Cruzeiro. 
Neste jogo, cada um deles escreve uma palavra escondida num papel e depois as comparam. Ganha
 quem tiver escrito a palavra que, em ordem alfabética (lexicográfica) vem "depois".

Por exemplo, se Andreia joga "ornitorrinco", mas Brocado joga "ornitopata", vence Andreia, 
pois a letra "r" vem depois do "p". 

Porém, depois de um tempo, as duas crianças cansam de ficar tentando "calcular" qual das 
duas palavras vence. Você, sendo um inteligente programador, se dispõe a ajudá-las escrevendo 
um programa que responde quem é o vencedor.
"""

palvrs = input().lower().split()
tamanhos = [len(list(palvrs[0])),len(list(palvrs[1]))]
ganhador = ''
if palvrs[1].startswith(palvrs[0]) and len(list(palvrs[1])) > len(list(palvrs[0])):
    print('B')
elif palvrs[0].startswith(palvrs[1]) and len(list(palvrs[0])) > len(list(palvrs[1])):
    print('A')
else:
    for i in range(0,min(tamanhos)):
        if ord(palvrs[0][i]) < ord(palvrs[1][i]):
            ganhador = "B"
            break
        elif ord(palvrs[0][i]) > ord(palvrs[1][i]):
            ganhador = 'A'
            break 
        else:
            pass
    print(ganhador)