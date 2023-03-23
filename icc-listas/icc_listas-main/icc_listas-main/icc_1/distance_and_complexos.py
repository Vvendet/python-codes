"""Leia quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano: (x 1 , y 1 ) e (x 2 , y 2 )
e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
((x2 − x1 )2 + (y2 − y1 )2)1/2

Leia também um número complexo z = a + bj e calcule seu módulo |z| (distância até a origem), mostrando 4 casas decimais após a vírgula, usando a fórmula:
|z| = ((a 2 + b 2 ))1/2

Note que Python possui complex como tipo de dados. Um número complexo tem um componente real e um componente imaginário, ambos representados pelo tipo float em Python (é possível acessá-los separadamente). """

p1 = input().split()
p2 = input().split()
z = input()
abs = 0
for i in range(0,list(z)-1):
    z = list(z)
    try:
        abs += (float(z[i + 1]) + float(z[i]))**2
    except:
        try:
            abs += float(z[i])**2
        except: 
            pass


    
d = ((float(p1[0]) - float(p2[0]))**2 + (float(p1[1]) - float(p2[1]))**2)**0.5
print("{d:.4f}".format(d=d))
print("{abs:.4f}".format(abs=abs**0.5))