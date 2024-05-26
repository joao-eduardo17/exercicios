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

# 1011 - Esfera
raio = int(input())
vol = (4/3) * 3.14159 * (raio**3)
print(f"VOLUME = {vol:.3f}")

# 1012 - Área
pass

# 1021 - Notas e Moedas
# nota = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}
# moeda = {100:0, 50:0, 25:0, 10:0, 5:0, 1:0}
# n = float(input())
# while n:
#     # NOTA
#     if n >= 100.00:
#         n -= 100.00
#         nota[100]+=1
#     elif n >= 50.00:
#         n -= 50.00
#         nota[50]+=1
#     elif n >= 20.00:
#         n -= 20.00
#         nota[20]+=1
#     elif n >= 10.00:
#         n -= 10.00
#         nota[10]+=1
#     elif n >= 5.00:
#         n -= 5.00
#         nota[5]+=1
#     elif n >= 2.00:
#         n -= 2.00
#         nota[2]+=1
#     # MOEDA
#     elif n >= 1.00:
#         n -= 1.00
#         moeda[100]+=1
#     elif n >= 0.50:
#         n -= 0.50
#         moeda[50]+=1
#     elif n >= 0.25:
#         n -= 0.25
#         moeda[25]+=1
#     elif n >= 0.10:
#         n -= 0.10
#         moeda[10]+=1
#     elif n >= 0.5:
#         n -= 0.5
#         moeda[5]+=1
#     elif n >= 0.01:
#         n -= 0.01
#         moeda[1]+=1



# print("NOTAS:")
# print(f"{n100} nota(s) de R$ 100.00")
# print(f"{n50} nota(s) de R$ 50.00")
# print(f"{n20} nota(s) de R$ 20.00")
# print(f"{n10} nota(s) de R$ 10.00")
# print(f"{n5} nota(s) de R$ 5.00")
# print(f"{n2} nota(s) de R$ 2.00")
# print("MOEDAS:")
# print(f"{m100} moeda(s) de R$ 1.00")
# print(f"{m50} moeda(s) de R$ 0.50")
# print(f"{m25} moeda(s) de R$ 0.25")
# print(f"{m10} moeda(s) de R$ 0.10")
# print(f"{m5} moeda(s) de R$ 0.05")
# print(f"{m1} moeda(s) de R$ 0.01")

# 1040 - Média 3
n = input().split()
media = (float(n[0]) * 0.2) + (float(n[1]) * 0.3) + (float(n[2]) * 0.4) + (float(n[3]) * 0.1)
x = str(media).find(".")
if media >= 7.0:
    print(f"Media: {str(media)[0:x+2]}")
    print("Aluno aprovado.")
elif media < 5.0:
    print(f"Media: {str(media)[0:x+2]}")
    print("Aluno reprovado.")
else:
    n2 = float(input())
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    print(f"Nota do exame: {n2:.1f}")
    media2 = (media + n2)/2
    if media2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {str(media2)[0:x+2]}")

# 1042 - Sort Simples
n = input().split()
l = []
for c in n:
    l.append(int(c))
l.sort()
for c in l:
    print(c)
print()
for c in n:
    print(c)

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

# 1045 - Tipos de Triângulos
nums = input().split()
n = [float(c) for c in nums]
n.sort(reverse=True)
a,b,c = n[0], n[1], n[2]
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif a**2 == ((b**2)+(c**2)):
    print("TRIANGULO RETANGULO")
elif a**2 > ((b**2)+(c**2)):
    print("TRIANGULO OBTUSANGULO")
elif a**2 < ((b**2)+(c**2)):
    print("TRIANGULO ACUTANGULO")

if a==b==c:
    print("TRIANGULO EQUILATERO")
elif a==b or a==c or b==c:
    print("TRIANGULO ISOSCELES")
        
# 1046 - Tempo de Jogo
n = input().split()
i,f = int(n[0]), int(n[1])
d = 0
if i == f:
    d = 24
else:
    while i != f:
        if i == 24:
            i = 0
        if i == f:
            break
        i+=1
        d+=1
print(f"O JOGO DUROU {d} HORA(S)")

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

# 1052 - Mês
n = int(input())
mes = "? January February March April May June July August September October November December".split()
print(mes[n])

# 1059 - Números Pares
for c in range(2,101, 2):
    print(c)

# 1060 - Números Positivos
k = 0
for c in range(6):
    n = float(input())
    if n > 0:
        k+=1
print(f"{k} valores positivos")

# 1144 - Sequência Lógica
n = int(input())
for c in range(1,n+1):
  print(f"{c} {c*c} {(c)*(c**2)}")
  print(f"{c} {(c*c)+1} {(c)*(c**2)+1}")

# 1153 - Fatorial Simples
n = int(input())
x = 1
while n>0:
    x *= n
    n -= 1
print(x)

# 1157 - Divisores I
n = int(input())
for c in range(1,n+1):
    if n%c == 0:
        print(c)

# 1589 - Bob Conduíte
n = int(input())
resp = []
for c in range(n):
    inp = input().split()
    x = int(inp[0]) + int(inp[1])
    resp.append(x)
for k in resp:
    print(k)

# 1933 - Tri-du
n = input().split()
if int(n[0]) > int(n[1]):
    print(n[0])
elif int(n[0]) < int(n[1]):
    print(n[1])
else:
    print(n[0])

# 1985 - MacPRONALTS
n = int(input())
v = 0
mc = {
    1001: 1.5,
    1002: 2.5,
    1003: 3.5,
    1004: 4.5,
    1005: 5.5
}
for c in range(n):
    n = input().split()
    x = mc[int(n[0])]
    v += (x*int(n[1]))
print(f"{v:.2f}")

# 2006 - Identificando o Chá
r = input()
rs = input().split()
x = rs.count(r)
print(x)

# 2061 - As Abas de Péricles
n = input().split()
aba = int(n[0])
for c in range(int(n[1])):
    fc = input()
    if "f" in fc:
        aba+=1
    else:
        aba-=1
print(aba)

# 2172 - Evento
xp = []
while True:
    n = input().split()
    if int(n[0]) == 0 and int(n[1]) == 0:
        break
    c = int(n[0]) * int(n[1])
    xp.append(c)
for c in xp:
    print(c)


# 2752 - Saída 6
print("<AMO FAZER EXERCICIO NO URI>")
print("<    AMO FAZER EXERCICIO NO URI>")
print("<AMO FAZER EXERCICIO >")
print("<AMO FAZER EXERCICIO NO URI>")
print("<AMO FAZER EXERCICIO NO URI    >")
print("<AMO FAZER EXERCICIO NO URI>")
print("<          AMO FAZER EXERCICIO >")
print("<AMO FAZER EXERCICIO           >")

# 2791 - Feijão
n = input().split()
k = 1
for c in n:
    if c == "1":
        break
    k+=1
print(k)

# 2936 - Quanta Mandioca?
n1 = int(input()) * 300
n2 = int(input()) * 1500
n3 = int(input()) * 600
n4 = int(input()) * 1000
n5 = int(input()) * 150
print(n1+n2+n3+n4+n5+225)

# 3046 - Dominó
n = int(input())
x = ((n+1)*(n+2))/2
print(int(x))

# 3055 - Nota Esquecida
nota = int(input())
media = int(input())
for c in range(0,101):
    if (nota+c)/2 == media:
        print(c)
        break
