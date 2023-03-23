data = input().split()
t1 = float(data[0]) - 30*60
desconto = 0
v1 = float(data[1]) - 60
d_s1 =0
if data[0] == 0:
    desconto += -1000
if int(t1) < 0:
    desconto += int(t1)*2
    d_s1 = desconto
elif int(t1) > 0:
    desconto += int(t1)*-1
    d_s1 = desconto
print(desconto)
if v1 > 0:
    v1 = v1*-1
    desconto += int(v1)*10 
print(desconto)

t2 = float(data[2]) - 60*60
desconto2 = 0
v2 = float(data[3]) - 40

if data[2] == 0:
    desconto += -1000
if int(t2) < 0:
    desconto2 += int(t2)*2
    d_s1 += desconto2
    
elif int(t2) > 0:
    desconto2 += int(t2)*-1
    d_s1 += desconto2
print(desconto2)


if v2 > 0:
    v2 = v2*-1
    desconto2 += int(v2)*20 
print(desconto2)

print(d_s1)
print(desconto + desconto2)