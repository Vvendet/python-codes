"""
Seu sobrinho Joberto está aprendendo a escrever e está tendo 
dificuldade de lembrar que deve usar letra maiúscula no início da frase.

Como um bom tio que é, e um exímio 
programador, você decide que a melhor 
abordagem é escrever um programa que faça as correções automaticamente."""

def capt(text):
    boole = True
    stri = ''
    for k in text:
        if boole == True and k != '.':
            if k != ' ' and k != '' and k != '.':
                stri += k.upper()
                boole = False
            else:
                stri += k
        elif k == '.' :
            stri += k
            boole = True
        else:
            stri += k
    return stri


text = capt(input(''))
print (text)
