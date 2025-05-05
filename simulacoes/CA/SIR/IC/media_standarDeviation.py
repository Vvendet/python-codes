import math

generations = 50
media = [0 for i in range(generations)] 
desvioPadrao =[0 for i in range(generations)]



# BLOCO DE CODIGO PARA CALCULAR MEDIA

for i in range(generations):
    file = "infectados" + str(i+1) +".dat" 
    with open(file) as f:
        for x in f:
            media[int(x.split()[0])-1]+=int(x.split()[1]) 
media = [media[i]/50 for i in range(generations)]

####

#BLOCO DE CODIGO PARA CALCULAR DESVIO PADRAO

for i in range(generations): 
    file = "infectados" + str(i+1) +".dat" 
    with open(file) as f:
        for x in f:
            desvioPadrao[int(x.split()[0])-1]+=(int(x.split()[1])-media[int(x.split()[0])-1])**2 
desvioPadrao =[math.sqrt(desvioPadrao[i]/50) for i in range(generations)]

######

with open('media_desvioPadrao.dat','a') as f:
    for i in range(generations):
        f.write(str(media[i-1])+"    ")
        f.write(str(desvioPadrao[i-1])+"\n")


