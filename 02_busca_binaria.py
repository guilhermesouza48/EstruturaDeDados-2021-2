# ALGORITMO DE BUSCA BINARIA

# Dada uma lista, que deve estar PREVIAMENTE ORDERNADA, e um valor de busca,
# divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que
# se encontre o valor de busca ou que reste apenas uma sublista vazia, quando se conclui
# que o valor de busca não existe na lista.

from time import time
from data.lista_nomes import nomes


comps = 0 #  Declarando uma variável global

def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritmo de busca binária

        Retorna a posição onde valor_busca foi encontrado ou o valor convencional -1 se valor_busca não existir na lista
    """
    ini = 0 #Primeira posição
    fim = len(lista) - 1 #Última posição

    global comps # Indica que estamos usando a variável declarada na linha 13

    comps = 0

    while ini <= fim:
        meio = ( ini + fim ) // 2 #Operador / é divisão inteira

        #1ºcaso: Lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca: #ENCONTROU!
            comps += 1
            return meio #Meio é a posição onde valor_busca está na lista

        #2ºcaso: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            comps += 2 
            fim = meio - 1 #Descarta a 2ºmetade da lista

        #3ºcaso: valor_busca é maior que lista[meio]
        else:
            comps += 2
            ini = meio + 1 #Descarta a 1ºmetade da lista

    #4ºcaso: valor_busca não encontrado na lista
    return -1

hora_ini = time()
print(f"Posição de HOTAVIO: {busca_binaria(nomes, 'HOTAVIO')}, {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando HOTAVIO: {(hora_fim - hora_ini) * 1000}ms")


print(f"Posição de HOTAVIO: {busca_binaria(nomes, 'HOTAVIO')}, {comps} comparações")
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}, {comps} comparações")

print(f"Nome exatamente no meio da lista: {nomes[len (nomes) // 2]}") 

hora_ini = time()
print(f"Posição de JEDERSON: {busca_binaria(nomes,'JEDERSON')}, {comps} comparações") 
hora_fim = time()
print(f"tempo gasto procurando JEDERSON: {(hora_fim - hora_ini) * 1000}ms ") 

hora_ini = time()
print(f"Posição de AARAO: {busca_binaria(nomes,'AARAO')}, {comps} comparações") 
hora_fim = time()
print(f"tempo gasto procurando AARAO: {(hora_fim - hora_ini) * 1000}ms ") 