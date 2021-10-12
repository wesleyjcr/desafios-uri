# https://www.urionlinejudge.com.br/judge/pt/problems/view/1022

from math import gcd


def soma(n1, d1, n2, d2):
    num = n1*d2 + n2*d1
    den = d1*d2
    return num, den

def subtracao(n1, d1, n2, d2):
    num = n1*d2 - n2*d1
    den = d1*d2
    return num, den

def multiplicacao(n1, d1, n2, d2):
    num = n1*n2 
    den = d1*d2
    return num, den

def divisao(n1, d1, n2, d2):
    num = n1*d2
    den = n2*d1
    return num, den     

def simplifica(num, den):
    mdc = gcd(num, den)
    num_sim = int(num / mdc)
    den_sim = int(den / mdc)
    return num_sim, den_sim

def apresentar(num, den, num_sim, den_sim):
    print(f'{num}/{den} = {num_sim}/{den_sim}')

num_entradas = int(input())

while num_entradas != 0:
    entrada = input().split()
    sinal = entrada[3]
    
    n1 = int(entrada[0])
    d1 = int(entrada[2])
    n2 = int(entrada[4])
    d2 = int(entrada[6])

    if sinal == '+':
        num, den = soma(n1, d1, n2, d2)
        num_sim, den_sim = simplifica(num, den)
        apresentar(num, den, num_sim, den_sim)
        
    elif sinal == '-':
        num, den = subtracao(n1, d1, n2, d2)
        num_sim, den_sim = simplifica(num, den)
        apresentar(num, den, num_sim, den_sim)

    elif sinal == '*':
        num, den = multiplicacao(n1, d1, n2, d2)
        num_sim, den_sim = simplifica(num, den)
        apresentar(num, den, num_sim, den_sim)

    elif sinal == '/':
        num, den = divisao(n1, d1, n2, d2)
        num_sim, den_sim = simplifica(num, den)
        apresentar(num, den, num_sim, den_sim)
    
    num_entradas -=1