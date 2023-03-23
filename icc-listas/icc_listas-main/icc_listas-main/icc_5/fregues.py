"""
John é garçom de um restaurante cujo prato de maior sucesso é a sopa de letrinhas. 
Para passar o tempo, ele fica procurando as letras do seu nome na sopa que entrega
 para os clientes.

Enquanto fazia isso, percebeu que, dentre as sopas que os clientes deixavam para trás
 ao sair, existia um padrão nas letrinhas restantes. As letras do seu nome sempre eram rejeitadas!

Frustrado e levemente assustado com a descoberta, John pede para que você escreva um 
programa para se certificar que não está ficando maluco.
"""
io = input()

io2 = input()

total = (list(io).count('J') + list(io).count('O') + list(io).count('H') + list(io).count('N')) + (list(io).count('j') + list(io).count('o') + list(io).count('h') + list(io).count('n'))

i2 = list(io2).count('J') + list(io2).count('O') + list(io2).count('H') + list(io2).count('N') + list(io2).count('j') + list(io2).count('o') + list(io2).count('h') + list(io2).count('n')

print(total-i2,i2)