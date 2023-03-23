"""
Faça um programa para ler 3 notas, e o número de faltas obtidas no 
semestre de cada um dos n alunos de uma disciplina. O valor de n 
(quantidade de alunos) deve ser informado pelo usuário. Calcular a nota 
final de cada aluno (dada pela média aritmética das 3 notas), e imprimir 
essa nota final com uma mensagem dizendo a situação final do aluno, ou seja, 
se o aluno foi “Aprovado”, ficou de “Exame” ou “Reprovado”:
"""

n = int(input())
notas = []
aprovados = 0
for i in range(0,n):
    a,b,c,d = input().split()
    a,b,c,d = [float(a),float(b),float(c),int(d)]
    media = (a+b+c)/3
    if media >= 5 and d <= 16:
        print(f'{media:.1f}', "Aprovado")
        aprovados += 1
    elif media > 3 and media < 5 and d <= 16:
        print(f'{media:.1f}', "Exame")
    elif media <= 3 or d > 16:
        print(f'{media:.1f}', "Reprovado")
    notas.append(media)
print(f'{sum(notas)/n:.1f}',aprovados)
