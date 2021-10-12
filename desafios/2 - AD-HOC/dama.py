# https://www.urionlinejudge.com.br/judge/pt/problems/view/1087


def entrada():
    entrada = input()
    return map(int, entrada.split(" "))


def processamento():
    if x1 == x2 and y1 == y2:
        return 0
    elif x1 == x2 or y1 == y2 or x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
        return 1
    else:
        return 2


x1, y1, x2, y2 = entrada()


while x1 + y1 + x2 + y2 != 0:
    print(processamento())
    x1, y1, x2, y2 = entrada()
