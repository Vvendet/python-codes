n = int(input()) 
'''lista que vai armazenar a tupla''' 
tabela = []

for i in range(n): 
    jogador, jogada = input().split() 
    jogada = int(jogada)
    
    '''
    inserindo a tupla formada pelo nome e o índice escolhido por cada
    jogador na lista na mesma ordem do input;
    '''
    tabela.append((jogador, (jogada - 1))) 
                                           
vencedor = ""
'''
o jogo deve ser iniciado pelo fim da lista, logo a primeira jogada
precisa começar pelo fim da lista, ou seja, n-1.
'''
jogada_atual = n - 1 
'''
lista que armazena as jogadas na ordem em que elas serão avaliadas
'''
jogadas_calculadas = []

while True:
    '''
    o [1] faz referência ao número escolhido pelo jogador de acordo
    com a última jogada. Em seguida, devo verificar esta jogada já
    está na lista de jogadas_calculadas, se isso ocorrer então vou
    armazenar o nome do jogador que escolheu o número. Para isso, eu
    levo em consideração a mesma jogada, porém com a referência do
    nome, o índice [0], e guardo na variável vencedor e o laço do
    while é parado.
    '''
    '''
    no primeiro laço de repetição, a lista de jogadas_calculadas
    está vazia, então vou cair no caso do else.
    '''
    if tabela[jogada_atual][1] in jogadas_calculadas:
        vencedor = tabela[jogada_atual][0]
        break
        '''
        o caso do else, é responsável por inserir a nova jogada na lista
        de jogadas_calculadas até que a condição do if seja satisfeita e
        o laço de repetição seja parado.
        '''
    else:
        jogadas_calculadas.append(jogada_atual)
        jogada_atual = tabela[jogada_atual][1]
                
print(vencedor)