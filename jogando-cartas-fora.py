#https://www.urionlinejudge.com.br/judge/pt/problems/view/1110


entrada = int(input())
descarte = []


while entrada != 0:
    lista = list(range(1, entrada + 1))
    
    while len(lista)>= 2: 
        descarte.append(lista[0])
        del lista[0]

        lista.append(lista[0])
        del lista[0]

    sobra = lista[0]
    print_result = ', '.join(str(e) for e in descarte)
    print(f'Discarded cards: {print_result}')
    print(f'Remaining card: {sobra}')    

    lista = []
    descarte = []
    sobra = None
    entrada = int(input())
