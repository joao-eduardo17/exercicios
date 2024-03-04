# 1000 - Hello World!
print("Hello World!")

# 1001 - Extremamente Básico
a = int(input())
b = int(input())
print(f"X = {a+b}")

# 1002 - Área do Círculo
raio = float(input())
area = 3.14159 * (raio**2)
print(f"A={area:.4f}")

# 1003 - Soma Simples
a = int(input())
b = int(input())
print(f"SOMA = {a+b}")

# 1004 - Produto simples
x = int(input())
y = int(input())
print(f"PROD = {x*y}")

# 1005 - Média 1
n1 = float(input()) * 3.5
n2 = float(input()) * 7.5
media = (n1 + n2)/11
print(f"MEDIA = {media:.5f}")

# 1006 - Média 2
a = float(input()) * 0.2
b = float(input()) * 0.3
c = float(input()) * 0.5
media = (a+b+c)
print(f"MEDIA = {media:.1f}")

# 1007 - Diferença
a = int(input())
b = int(input())
c = int(input())
d = int(input())
dif = (a*b) - (c*d)
print(f"DIFERENCA = {dif}")

# 1008 - Salário
num = input()
hor = float(input())
sal = float(input())
print(f"NUMBER = {num}")
print(f"SALARY = U$ {hor*sal:.2f}")

# 1009 - Salário com Bônus´
nome = input()
sal = float(input())
ven = float(input())
com = ven * 0.15
print(f"TOTAL = R$ {sal+com:.2f}")

# 1010 - Cálculo Simples
p1 = input().split()
p2 = input().split()
vp1 = float(p1[2]) * int(p1[1])
vp2 = float(p2[2]) * int(p2[1])
print(f"VALOR A PAGAR: R$ {vp1+vp2:.2f}")


# 1043 - Triângulo
nums = input().split()
a,b,c = float(nums[0]), float(nums[1]), float(nums[2])
if abs(b-c) < a and a < b+c:
    if abs(a-c) < b and b < a+c:
        if abs(a-b) < c and c < a+b:
            print(f"Perimetro = {a+b+c:.1f}")
        else:
            print(f"Area = {((a+b)*c)/2:.1f}")
    else:
        print(f"Area = {((a+b)*c)/2:.1f}")
else:
    print(f"Area = {((a+b)*c)/2:.1f}")

# 1044 - Múltiplos
nums = input().split()
a,b = int(nums[0]), int(nums[1])
if a > b:
    if a%b == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif b > a:
    if b%a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    print("Sao Multiplos")

# 1045 - Tipos de Triângulos - ERRADIO <Adbnjkfaebhjkjld
nums = input().split()
l = [float(i) for i in nums]
a = max(l)
ind = l.index(a)
l.pop(ind)
b,c = float(l[0]), float(l[1])
while True:
    if a >= (b+c):
        print("NAO FORMA TRIANGULO")
        break
    if (a**2) == ((b**2 )+ (c**2)):
        print("TRIANGULO RETANGULO")
        break
    if (a**2) > ((b**2 )+ (c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < ((b**2 )+ (c**2)):
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
        break
    elif (a==b)!=c or (a==c)!=b or (b==c)!=a:
        print("TRIANGULO ISOSCELES")
        break
        
# 1046 - Tempo de Jogo
nums = input().split()
ini, fim = int(nums[0]), int(nums[1])
while True:
    if ini == fim:
        print("O JOGO DUROU 24 HORA(S)")
        break
    tempo = 0
    for c in range(1,24):
        if ini == fim:
            tempo = c
            break
        if ini == 23:
            ini = 0
        ini += 1
    print(f"O JOGO DUROU {tempo} HORA(S)")
    break

# 1048 - Aumento de Salário
sal = float(input())
if sal < 400.01:
    pr = "15 %"
    r = sal * 0.15
elif sal < 800.01:
    pr = "12 %"
    r = sal * 0.12
elif sal < 1200.01:
    pr = "10 %"
    r = sal * 0.1
elif sal < 2000.01:
    pr = "7 %"
    r = sal * 0.07
else:
    pr = "4 %"
    r = sal * 0.04
print(f"Novo salario: {sal + r:.2f}")
print(f"Reajuste ganho: {r:.2f}")
print(f"Em percentual: {pr}")

# 1049 - Animal
p1 = input()
p2 = input()
p3 = input()
if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if p3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if p3 == 'onivoro':
            print('minhoca')
        else:
            print('sanguessuga')

# 1050 - DDD
ddd = int(input())
match(ddd):
    case 61:
        print('Brasilia')
    case 71:
        print('Salvador')
    case 11:
        print('Sao Paulo')
    case 21:
        print('Rio de Janeiro')
    case 32:
        print('Juiz de Fora')
    case 19:
        print('Campinas')
    case 27:
        print('Vitoria')
    case 31:
        print('Belo Horizonte')
    case default:
        print('DDD nao cadastrado')

