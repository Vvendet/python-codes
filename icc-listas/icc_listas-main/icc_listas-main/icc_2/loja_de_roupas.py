inp = input().split()
val = float(inp[0])
n = int(inp[1])
val_final = 0
if n == 1:
    val_final = val - 5*val/100
    print("{d:.2f}".format(d=val_final),end=' ')
    print("{d:.2f}".format(d=val_final/1),end='')
elif n == 2:
    val_final = val
    print("{d:.2f}".format(d=val_final),end=' ')
    print("{d:.2f}".format(d=val_final/2),end='')
elif n == 3:
    val_final = val + val*5/100
    print("{d:.2f}".format(d=val_final),end=' ')
    print("{a:.2f}".format(a=val_final/3))
elif n == 4:
    val_final = val + val*10/100
    print("{d:.2f}".format(d=val_final),end=' ')
    print("{d:.2f}".format(d=val_final/4))