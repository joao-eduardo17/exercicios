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
nota = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}
moeda = {100:0, 50:0, 25:0, 10:0, 5:0, 1:0}
n = float(input())
while n:
    # NOTA
    if n >= 100.00:
        n -= 100.00
        nota[100]+=1
    elif n >= 50.00:
        n -= 50.00
        nota[50]+=1
    elif n >= 20.00:
        n -= 20.00
        nota[20]+=1
    elif n >= 10.00:
        n -= 10.00
        nota[10]+=1
    elif n >= 5.00:
        n -= 5.00
        nota[5]+=1
    elif n >= 2.00:
        n -= 2.00
        nota[2]+=1
    # MOEDA
    elif n >= 1.00:
        n -= 1.00
        moeda[100]+=1
    elif n >= 0.50:
        n -= 0.50
        moeda[50]+=1
    elif n >= 0.25:
        n -= 0.25
        moeda[25]+=1
    elif n >= 0.10:
        n -= 0.10
        moeda[10]+=1
    elif n >= 0.5:
        n -= 0.5
        moeda[5]+=1
    elif n >= 0.01:
        n -= 0.01
        moeda[1]+=1



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

# 1047 - Tempo de Jogo com Minutos
n = input().split()
l = [int(c) for c in n]
i,m1,f,m2 = l[0], l[1], l[2], l[3]
h,m = 0,0
if i == f and m1 == m2:
    h = 24
else:
    if m1 == m2:
        pass
    else:
        if m2 > m1:
            m = m2 - m1
        else:
            m = 60-(m1-m2)
            i+=1
    while i != f:
        if i == 24:
            i = 0
        if i == f:
            break
        i+=1
        h+=1
print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")

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

# fudeu
sal = float(input())
ir = 0
if sal < 2000.00:
    print("Isento")
else:
    x = sal - 2000.01
    ir += sal * 0.08
    if sal > 2500.00:
        x = sal - 2500.00
        ir += x * 0.28
    if sal > 1000.00:
        x = sal - 1000.00
        ir += x * 0.18
print(f"R$$ {ir:.2f}")

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

# 1061 - NAO ACABOU
n = input().split()
d = n[1]
n = input().split()
x,y,z = int(n[0]), int(n[2]), int(n[4])
n = input().split()
d1 = n[1]
n = input().split()
x1,y1,z1 = int(n[0]), int(n[2]), int(n[4])
dia,h,m,s = 0,0,0,0

if z != z1:
    if z > z1:
        s = 60-(z-z1)
        y+=1
    else:
        s = z1-z
if y != y1:
    if y > y1:
        m = 60-(y-y1)
    else:
        m = y1-y

# 1064 - Positivos e Média
p,m = 0,0
for c in range(6):
    n = float(input())
    if n >= 0:
        p+=1
        m+=n
print(f"{p} valores positivos")
print(f"{m/p:.1f}")

# 1065 - Pares entre Cinco Números
p = 0
for c in range(5):
    n = int(input())
    if n%2 == 0:
        p+=1
print(f"{p} valores pares")

# 1066 - Pares, Ímpares, Positivos e Negativos
p,i,pos,neg = 0,0,0,0
for c in range(5):
    n = int(input())
    if n%2 == 0:
        p+=1
    else:
        i+=1
    if n > 0:
        pos+=1
    if n < 0:
        neg+=1
print(f"{p} valor(es) par(es)")
print(f"{i} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")

# 1067 - Números Ímpares
n = int(input())
for c in range(1,n+1, 2):
    print(c)

# 1070 - Seis Números Ímpares
n = int(input())
if n%2 == 0:
    n+=1
    print(n)
    for c in range(5):
        n+=2
        print(n)
else:
    for c in range(6):
        print(n)
        n+=2

# 1071
n1 = int(input())
n2 = int(input())
if n1%2 == 1:
    if n2%2 == 1:
        print(n1+n2)
    else:
        print(n1)
else:
    if n2%2 == 1:
        print(n2)
    else:
        print(0)

# 1072 - Intervalo 2
n = int(input())
i,o = 0,0
for c in range(n):
    l = int(input())
    if l >= 10 and l <= 20:
        i+=1
    else:
        o+=1
print(f"{i} in")
print(f"{o} out")

# 1073 - Quadrado de Pares
n = int(input())
if n%2 == 0:
    for c in range(2,n+1,2):
        print(f"{c}^2 = {c**2}")
else:
    for c in range(2,n,2):
        print(f"{c}^2 = {c**2}")

# 1074 - Par ou Ímpar
n = int(input())
l = []
for c in range(n):
    i = int(input())
    l.append(i)
for c in l:
    if c == 0:
        print("NULL")
        continue
    elif c%2 == 0:
        if c > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if c > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")

# 1075 - Resto 2
n = int(input())
for c in range(1,10001):
    if c%n == 2:
        print(c)

# 1078 - Tabuada
n = int(input())
for c in range(1,11):
    print(f"{c} x {n} = {n*c}")

# 1079 - Médias Ponderadas
n = int(input())
r = []
for c in range(n):
    nums = input().split()
    a,b,c = float(nums[0]) * 0.2, float(nums[1]) * 0.3, float(nums[2]) * 0.5
    r.append((a+b+c))
for c in r:
    print(f"{c:.1f}")

# 1080 - Maior e Posição
nums = []
for c in range(100):
    n = int(input())
    nums.append(n)
mx = max(nums)
print(mx)
print(nums.index(mx)+1)

# 1094 - Experiências
n = int(input())
c,r,s = 0,0,0
for k in range(n):
    ex = input().split()
    if ex[1] == "C":
        c+=int(ex[0])
    elif ex[1] == "R":
        r+=int(ex[0])
    else:
        s+=int(ex[0])
tot = c+r+s
print(f"Total: {tot} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {(100*c)/tot:.2f} %")
print(f"Percentual de ratos: {(100*r)/tot:.2f} %")
print(f"Percentual de sapos: {(100*s)/tot:.2f} %")

# 1095 - Sequencia IJ 1
i,j = -2,65
while j != 0:
    i+=3
    j-=5
    print(f"I={i} J={j}")

# 1096 - Sequencia IJ 2
i = 1
while i <= 9:
    print(f"I={i} J=7")
    print(f"I={i} J=6")
    print(f"I={i} J=5")
    i+=2

# 1097 - Sequencia IJ 3
i,j = 1, 7
while i <= 9:
    print(f"I={i} J={j}")
    print(f"I={i} J={j-1}")
    print(f"I={i} J={j-2}")
    i+=2
    j+=2

# 1098 - Sequencia IJ 4 (nao finalizado)
i,j,c = -1,0,5
while i < 2:
    if c == 5:
        i+=1
        j+=1
        print(f"I={int(i)} J={int(j)}")
        print(f"I={int(i)} J={int(j+1)}")
        print(f"I={int(i)} J={int(j+2)}")
        c = 0
    else:
        print(f"I={i:.1f} J={j:.1f}")
        print(f"I={i:.1f} J={j+1:.1f}")
        print(f"I={i:.1f} J={j+2:.1f}")
    i+=0.2
    j+=0.2
    c+=1

# 1099 - Soma de Ímpares Consecutivos II
n = int(input())
r = []
for c in range(n):
    i = input().split()
    p = [int(k) for k in i]
    soma = 0
    for o in range(min(p)+1, max(p)):
        if o%2 == 1:
            soma+=o
    r.append(soma)
for c in r:
    print(c)

# 1101 Sequência de Números e Soma
r = []
while True:
    l = []
    n = input().split()
    l = [int(k) for k in n]
    if l[0] <= 0 or l[1] <= 0:
        break
    resp,soma = "",0
    for c in range(min(l), max(l)+1):
        soma += c
        resp += str(c) + " "
    resp += "Sum=" + str(soma)
    r.append(resp)
for c in r:
    print(c)

# 1113 - Crescente e Decrescente
r = []
while True:
    l = []
    n = input().split()
    l = [int(k) for k in n]
    if n[0] == n[1]:
        break
    if l[0] > l[1]:
        r.append("Decrescente")
    else:
        r.append("Crescente")
for c in r:
    print(c)

# 1114 - Senha Fixa
r = []
while True:
    n = int(input())
    if n == 2002:
        r.append("Acesso Permitido")
        break
    else:
        r.append("Senha Invalida")
for c in r:
    print(c)

# 1115 - Quadrante
r = []
while True:
    l = []
    n = input().split()
    l = [int(c) for c in n]
    if l[0] == 0 or l[1] == 0:
        break
    if l[0] > 0:
        if l[1] > 0:
            r.append("primeiro")
        else:
            r.append("quarto")
    else:
        if l[1] > 0:
            r.append("segundo")
        else:
            r.append("terceiro")
for c in r:
    print(c)

# 1116 - Dividindo X por Y
n = int(input())
r = []
for c in range(n):
    i = input().split()
    l = []
    l = [int(c) for c in i]
    if l[1] == 0:
        r.append("divisao impossivel")
    else:
        r.append(l[0]/l[1])
for k in r:
    print(k)

# 1117 - Validação de Nota
media,c,ni = 0,0,0
while True:
    if c == 2:
        break
    n = float(input())
    if n < 0 or n > 10:
        ni+=1
        continue
    media+=n
    c+=1
for c in range(ni):
    print("nota invalida")
print(f"media = {media/2:.2f}")

# 1118 - Várias Notas Com Validação
r = []
c,media = 0,0
while True:
    if c == 2:
        i = int(input())
        r.append("novo calculo (1-sim 2-nao)")
        if i != 1 and i != 2:
            continue
        if i == 1:
            c = 0
            continue
        else:
            break
    i = float(input())
    if i > 10 or i < 0:
        r.append("nota invalida")
        continue
    media+=i
    c+=1
    if c == 2:
        r.append(f"media = {media/2:.2f}")
        media = 0
for k in r:
    print(k)


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
