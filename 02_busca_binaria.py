# ALGORITMO DE BUSCA BINARIA

# Dada uma lista, que deve estar PREVIAMENTE ORDERNADA, e um valor de busca,
# divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que
# se encontre o valor de busca ou que reste apenas uma sublista vazia, quando se conclui
# que o valor de busca não existe na lista.

from time import time
from data.lista_nomes import nomes

def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritmo de busca binária

        Retorna a posição onde valor_busca foi encontrado ou o valor convencional -1 se valor_busca não existir na lista
    """
    ini = 0 #Primeira posição
    fim = len(lista) - 1 #Última posição

    while ini <= fim:
        meio = ( ini + fim ) // 2 #Operador / é divisão inteira

        #1ºcaso: Lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca: #ENCONTROU!
            return meio #Meio é a posição onde valor_busca está na lista

        #2ºcaso: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            fim = meio - 1 #Descarta a 2ºmetade da lista

        #3ºcaso: valor_busca é maior que lista[meio]
        else:
            ini = meio + 1 #Descarta a 1ºmetade da lista

    #4ºcaso: valor_busca não encontrado na lista
    return -1

hora_ini = time()
print(f"Posição de HOTAVIO: {busca_binaria(nomes, 'HOTAVIO')}")
hora_fim = time()
print(f"Tempo gasto procurando HOTAVIO: {(hora_fim - hora_ini) * 1000}ms")


print(f"Posição de HOTAVIO: {busca_binaria(nomes, 'HOTAVIO')}")
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}")
