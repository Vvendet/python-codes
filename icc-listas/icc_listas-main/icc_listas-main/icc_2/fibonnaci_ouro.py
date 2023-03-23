serie = [1,1,2]

def value(n):
    number = (1/5**0.5)*(((1+5**0.5)/2)**n - ((1-5**0.2)/2)**n)
    return number

n = int(input())
print(f'{value(n+1)/value(n)}')
