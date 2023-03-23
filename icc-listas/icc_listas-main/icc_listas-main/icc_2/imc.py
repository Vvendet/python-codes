"""

Usando como dados de entrada altura h (em metros) e peso p (em quilos), elabore um programa que calcule o IMC (índice de massa corporal) do usuário, usando a fórmula:

IMC =p/h2 

Depois interprete e informe o resultado, da seguinte forma:"""

p = float(input())
h = float(input())

imc = p/(h*h)

if imc < 18.5:
    print(f'{imc:.2f}')
    print("Baixo peso")
elif imc <= 24.9 and imc >= 18.5:
    print(f'{imc:.2f}')
    print("Peso normal")
elif imc > 24.9 and imc <= 29.9:
    print(f'{imc:.2f}')
    print("Sobrepeso")
    print(f'{(p -(24.9*h*h)):.2f}')
elif imc > 29.9 and imc <= 34.9:
    print(f'{imc:.2f}')
    print("Obesidade grau I")
    print(f'{(p -(24.9*h*h)):.2f}')
elif imc > 34.9 and imc <= 39.9:
    print(f'{imc:.2f}')
    print("Obesidade grau II")
    print(f'{(p -(24.9*h*h)):.2f}')
elif imc > 39.9:
    print(f'{imc:.2f}')
    print("Obesidade grau III")
    print(f'{(p -(24.9*h*h)):.2f}')