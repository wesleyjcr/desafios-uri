# https://www.urionlinejudge.com.br/judge/pt/problems/view/1071


x = int(input())
y = int(input())
soma = 0

if x < y:
    lista = list(range(x + 1, y))
else:
    lista = list(range(y + 1, x))

for item in lista:
    if item % 2 == 1:
        soma += item

print(soma)
