# 1168 - LED
n = int(input())
d = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
resp = []
for c in range(n):
    soma = 0
    num = input()
    for k in num:
        soma += d[int(k)]
    resp.append(soma)

for r in resp:
    print(f"{r} leds")