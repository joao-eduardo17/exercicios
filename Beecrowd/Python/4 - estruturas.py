# 1022 - TDA Racional - ERRADO
n = int(input())
r = []
for c in range(n):
    op = input().split()
    n1,d1 = int(op[0]),int(op[2])
    sin = op[3]
    n2,d2 = int(op[4]),int(op[6])
    x1 = d1*d2
    match(sin):
        case "+":
            x = ((n1*d2)+(n2*d1))
        case "-":
            x = ((n1*d2)-(n2*d1))
        case "*":
            x = (n1*n2)
        case "/":
            x = n1*d2
            x1 = n2*d1
    cru = str(x)+"/"+str(x1)
    while True:
        if x%2 == 0 and x1%2 == 0:
            x = x//2
            x1 = x1//2
            continue
        if x%3 == 0 and x1%3 == 0:
            x = x//3
            x1 = x1//3
            continue
        if x == x1:
            x = 1
            x1 = 1
        break
    fmt = str(x) + "/" + str(x1)
    total = cru + " = " + fmt
    r.append(total)
for c in r:
    print(c)