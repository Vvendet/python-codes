def extraLongFactorials(n):
    # Write your code here
    if n == 1:
        return 1
    else:
        return (n * extraLongFactorials(n-1))

extraLongFactorials(25)