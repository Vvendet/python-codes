#Faça um programa que leia 5 números reais e calcule a média ponderada desses números.

nums = []
for i in range(0,5):
    a = float(input())
    nums.append(a)
m = 0
for i in range(0,len(nums)):
    m += nums[i]* (i + 1)
print("{media:.3f}".format(media=m/15))