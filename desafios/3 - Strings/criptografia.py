# https://www.urionlinejudge.com.br/judge/pt/problems/view/1024


def desloca_letras_direita(entrada):
    saida = ""
    for item in entrada:
        if item.isalpha():
            saida += chr(ord(item) + 3)
        else:
            saida += item
    return saida


def inverte_string(entrada):
    return entrada[::-1]


def desloca_letras_esquerda(entrada):
    saida = ""
    tamanho_texto = len(entrada)

    for index, item in enumerate(entrada):
        if index + 1 > tamanho_texto / 2:
            saida += chr(ord(item) - 1)
        else:
            saida += item

    return saida


numero_strings = int(input())

while numero_strings != 0:
    entrada = input()
    primeiro_passo = desloca_letras_direita(entrada)
    segundo_passo = inverte_string(primeiro_passo)
    terceiro_passo = desloca_letras_esquerda(segundo_passo)
    print(terceiro_passo)
    numero_strings -= 1
