senha = input()
valid = True
if len(senha) >= 4 and len(senha) <=20:
    number = 99999
    for i in list(senha):
        try:
            if int(i) < number:
                number = int(i)
            else:
                valid = False
        except:
            pass
else:
    valid = False

if valid:
    print("v")
else:
    print('n')
