def h(qdc, pa, destino):
    global quant_passos 
    if quant_passos > 0:
        if qdc > 1:
            auxiliar = ""
            if ((pa == "principal" and destino == "final") or
                (pa == "final" and destino == "principal")):
                auxiliar = "auxiliar"
            elif ((pa == "auxiliar" and destino == "final") or
                (pa == "final" and destino == "auxiliar")):
                auxiliar = "principal"
            else:
                auxiliar = "final"
            h(qdc - 1, pa,  auxiliar)
    
    if quant_passos > 0:
        disco = 0
        if pa == "principal":
            disco = pp.pop()
        elif pa == "auxiliar":
            disco = pino_auxiliar.pop()
        else:
            disco = pino_final.pop()

        if destino == "principal":
            pp.append(disco)
        elif destino == "auxiliar":
            pino_auxiliar.append(disco)
        else:
            pino_final.append(disco)

        quant_passos -= 1

    if quant_passos > 0:
        if qdc > 1:
            auxiliar = ""
            if ((pa == "principal" and destino == "final") or
                (pa == "final" and destino == "principal")):
                auxiliar = "auxiliar"
            elif ((pa == "auxiliar" and destino == "final") or
                (pa == "final" and destino == "auxiliar")):
                auxiliar = "principal"
            else:
                auxiliar = "final"          
            h(qdc - 1, auxiliar, destino)

pp = []
pino_auxiliar = []
pino_final = []

quant_discos, quant_passos = input().split()

quant_discos, quant_passos = int(quant_discos), int(quant_passos)
for disco in range(quant_discos, 0, -1):
    pp.append(disco)

h(quant_discos, "principal", "final")
print(len(pp), len(pino_auxiliar), len(pino_final))
