st =input()
res = st.split('_')
t = True
for i in range(len(res)):
    res[i] = list(res[i])
for i in res:
    for j in i:
        if t:
            print(j.upper(),end='')
            t = False
        else:
            print(j,end='')
    t = True
    