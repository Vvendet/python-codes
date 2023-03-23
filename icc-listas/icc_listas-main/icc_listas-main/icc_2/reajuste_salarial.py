cargo = input()
tempo_servico = int(input())
salario = float(input())
reajuste = 0
if salario < 1039:
    print("Salário inválido!")
else:
    if cargo == 'Gerente':
        if tempo_servico <= 3:
            reajuste = 12*salario/100
            salario += reajuste
            print(f'{reajuste:.2f}')
            print(f'{salario:.2f}')

        elif tempo_servico > 3 and tempo_servico <= 6:
            reajuste = 13*salario/100
            salario += reajuste
            print(f'{reajuste:.2f}')
            print(f'{salario:.2f}')

        elif tempo_servico > 6:
            reajuste = 15*salario/100
            salario += reajuste
            print(f'{reajuste:.2f}')
            print(f'{salario:.2f}')
    elif cargo == "Engenheiro":
        if tempo_servico <= 3:
            reajuste = 7*salario/100
            salario += reajuste
            print(f'{reajuste:.2f}')
            print(f'{salario:.2f}')
        elif tempo_servico > 3 and tempo_servico <= 6:
            reajuste = 11*salario/100
            salario += reajuste
            print(f'{reajuste:.2f}')
            print(f'{salario:.2f}')
        elif tempo_servico > 6:
            reajuste = 14*salario/100
            salario += reajuste
            print(f'{reajuste:.2f}')
            print(f'{salario:.2f}')
    else:
        reajuste = 5*salario/100
        salario += reajuste
        print(f'{reajuste:.2f}')
        print(f'{salario:.2f}')