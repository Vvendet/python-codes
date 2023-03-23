"""
dado um número n maior que 0, printe todos os divisores de n.
"""

n = int(input())
a = []
b = n
while b > 0:
    if n%b == 0:
        a.append(b)
    b -= 1

for i in a[::-1]:

    print(i)