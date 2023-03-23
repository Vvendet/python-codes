"""Raphael quer fazer um calendário para o mês atual. Para isso, ele desenha um tabela aonde as colunas correspondem às semanas (uma semana são 7 dias consecutivos de segunda até domingo), linhas  correspondem aos dias da semana, e as células contém datas. Por exemplo, o calendário para Janeiro de 2017 seria como na imagem abaixo:"""


entrada = input().split()
m = int(entrada[0])
d = int(entrada[1])

if m%2 != 0 and m < 8:
    if d >= 6:
        print(6)
    else:
        print(5)
elif m == 2 :
    if d <= 2:
        print(4)
    else:
        print(5)
else:
    if m%2 == 0:
        if d>= 6:
            print(6)
        else:
            print(5)
    elif m%2 != 0:
        
        if d == 7:
            print(6)
        else:
            print(5)
