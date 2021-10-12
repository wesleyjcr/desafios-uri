# https://www.urionlinejudge.com.br/judge/pt/problems/view/1087


entrada = input().split(" ")
x1, y1, x2, y2 = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])
while x1 + y1 + x2 + y2 != 0:
    if x1 == x2 and y1 == y2:
        print(0)
    elif x1 == x2 or y1 == y2 or x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
        print(1)
    else:
        print(2)
    entrada = input().split(" ")
    x1, y1, x2, y2 = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])
