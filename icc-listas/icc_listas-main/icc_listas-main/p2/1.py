a = True

def erro(l):
    for i in s:
        if i != '1' and i != '0':
            return True
    return False
while a:
    s = input()
    if s == "fim":
        a = False
    else:    
        s = list(s)
        
        if erro(s):
            print("erro")
        else:
            c = s.count('1')
            if c%2 == 0:
                print(0)
            else:
                print(1)
        