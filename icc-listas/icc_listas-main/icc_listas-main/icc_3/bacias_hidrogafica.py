"""
Para fins de estudos hidrológicos, uma Bacia Hidrográfica (BH) é considerada um 
conjunto de terras drenadas por um corpo d'água principal e seus a afluentes. 
A precipitação, a cobertura florestal e o tipo de solo/subsolo infuenciam na 
vazão dos rios de uma BH. Analise os dados e determine a BH com o maior índice pluviométrico anual, 
a BH com a estação de menor índice pluviométrico e a área média de uma BH.

"""

n = int(input())
lista = []
indices = []
menor = 9999999999
nome_menor = ''
areas = 0
indices2 = []
for i in range(0,n):
    info = input().split()
    nome = info[0]
    area = float(info[1])
    ipv = float(info[2])
    ipo = float(info[3])
    ipi = float(info[4])
    ipp = float(info[5])
    lista.append([nome,ipv + ipo + ipi + ipp])
    indices.append(ipv + ipo + ipi + ipp)
    idc = [ipv,ipo,ipi,ipp]
    for i in idc:
        if i < menor:
            menor = i
            nome_menor = nome
    
    areas += area


for i in lista:
    if max(indices) == i[1]:
        print(i[0])
print(nome_menor)
print(f'{areas/n:.2f}')