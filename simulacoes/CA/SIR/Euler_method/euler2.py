S = [9015]
I = [985]
t = 0
cont =  0
dt = 0.001
def WriteData(file, message1, message2): #função para escrever os dados nos arquivos

    with open(file,'a') as file:
        file.write(f"{message1}    ")
        file.write(f"{message2}\n")


while cont <10000:
	S.append(S[-1]-dt*1.9098300562505255*S[-1]*I[-1])
	I.append(I[-1]+dt*(1.9098300562505255*S[-1]*I[-1]-(1/7)*I[-1]))
	t += dt
	cont +=1
	WriteData('I.dat', str(t), str(I[-1]))
	WriteData("S.dat", str(t), str(S[-1]))
