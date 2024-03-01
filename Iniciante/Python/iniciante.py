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
