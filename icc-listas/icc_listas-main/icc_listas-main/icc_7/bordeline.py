N = int(input())

keyemotion = {}

for i in range(N):
    inp = input().split()
    keyemotion[inp[0]] = inp[1]

string = input().split()

res = []
for k in string:
    if k in keyemotion:
        res.append(keyemotion[k])
if res != []:
    res = ' '.join(res)
    print(res)
else:
    print('Tudo bem!')