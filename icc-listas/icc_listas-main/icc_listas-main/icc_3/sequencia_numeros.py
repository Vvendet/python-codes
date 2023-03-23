"""
Faça um programa que peça ao usuário para digitar uma sequência de inteiros. 
O programa deve parar quando 0 for digitado, que será desconsiderado na sequência 
de números lidos. No final,  você deve apresentar a quantidade de números lidos, 
o maior inteiro e a média aritmética simples dos inteiros.
"""

number = int(input())
numeros = []
while number != 0:
    if number != 0:    
        numeros.append(number)
    number = int(input())
print(len(numeros))

soma = 0
if len(numeros) > 0:
    print(max(numeros))
else:
    print(0)
for j in numeros:
    soma += j
try:
    print(f'{soma/len(numeros):.2f}')
except:
    print(f'{soma:.2f}')