x =  input()
y = input()

if x == y:
    print(-1)
elif len(x) > len(y):
    print(len(x))
else:
    print(len(y))