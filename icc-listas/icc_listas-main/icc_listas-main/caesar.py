

def caesarCipher(s, k):
    # Write your code here
    
    s_coded = []
    while k > 26:
        k -= 26
    for i in list(s):

        if ord(i) <= 90 and ord(i)>= 65:
            
            if ord(i) + k > ord('Z'):
                s_coded.append(chr(ord(i) + k - ord('Z') + ord('A')-1))
            else:
                s_coded.append(chr(ord(i) + k))

        elif ord(i) <= 122 and ord(i)>= 97:
            if ord(i) + k > ord('z'):
                s_coded.append(chr(ord(i) + k - ord('z') + ord('a')-1))
            else:
                s_coded.append(chr(ord(i) + k))

        else:
            s_coded.append(i)
    return "".join(s_coded)


s = input()

k = int(input().strip())

result = caesarCipher(s, k)

print(result)