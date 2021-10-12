# https://www.urionlinejudge.com.br/judge/pt/problems/view/2486

alimentos = {
    'suco_de_laranja': 120,
    'morango_fresco': 85,
    'mamao': 85,
    'goiaba_vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34,
}

vitamina_c = {
    'min': 110,
    'max': 130
}

consumo = 0

def retorna_quantidade_alimento(alimento):
    return int(alimento.split(' ')[0])

def retorna_nome_alimento(alimento):
    nome_alimento = alimento.split(' ')
    del(nome_alimento[0])
    return '_'.join(nome_alimento)



num_alimentos = int(input())
while num_alimentos != 0:
    for i in range(num_alimentos):
        alimento = input()

        quantidade = retorna_quantidade_alimento(alimento)
        nome_alimento = retorna_nome_alimento(alimento)

        consumo = consumo + (quantidade * alimentos[nome_alimento])
    
    if consumo < vitamina_c['min']:
        print(f"Mais {vitamina_c['min'] - consumo} mg")

    elif consumo > vitamina_c['max']:
        print(f"Menos {consumo - vitamina_c['max']} mg")
    else:
        print(f'{consumo} mg')    
    
    consumo = 0
    
    num_alimentos = int(input())

    
    


