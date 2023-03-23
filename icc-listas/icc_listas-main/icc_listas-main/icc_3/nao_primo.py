"""
Raphael e Renata estão cursando Teoria dos Números juntos. 
Certo dia eles se deparam com a seguinte hipótese: "Para todo inteiro positivo n e m temos 
que n⋅m + 1 é um número primo". Porém, eles percebem que essa hipótese é falsa, pois a Renata 
rapidamente nota que basta usar m = n - 2, assim:

n⋅m + 1 = n(n - 2) + 1 = (n -1)2

que não é primo.

De modo que para n > 2, m pode ser n - 2, e ainda inteiro positivo, e o resultado da hipótese 
não é primo. Por exemplo, se n = 7, então 7⋅5 + 1 = 36. Para n <= 2, podemos usar m = n + 2 como 
outro contra-exemplo. Entretanto, Raphael quer impressionar a Renata apresentando não apenas 
qualquer contra-exemplo, mas sim o menor m tal que n⋅m + 1 não seja primo para um dado n 
(por exemplo, para n = 7, poderíamos usar m = 1).

Você pode escrever um programa para ajudá-lo, dado o inteiro n?


"""

n = int(input())
m = 1
abra = True
while abra:
    primo = n*m + 1
    c = primo -1
    while c > 1:
        if primo%c == 0:
            abra = False
            print(m)
            break
        c -= 1
    m += 1


