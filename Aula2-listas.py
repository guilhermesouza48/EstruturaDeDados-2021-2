# Criando uma lista
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Percurso
for num in primos:
    print(num)

# Acrescentar um novo elemnto no FIM  da lista: append ()
primos.append(31)
print(primos)

# Inserindo um elemnto em uma posição específica: insert ()
# 1º -> informa a posição de inserção
# 2º -> elemento a ser inserido
primos.insert(0, 1)
print(primos)

primos.insert(5,37)# insere o valor 37 na posição 5
print(primos)

# Retirar o último elemento da lista: pop()
ultimo = primos.pop()
print(f"Último:{ultimo}")
print(primos)

# Removendo por valor: remove()
primos.remove(37)
print(primos)

# Removendo por posição: del
del primos[4]# removeno o elemnto da posição 4
print(primos)

# Fatiando uma lista
print(primos[0:7])# exibindo apenas do elemento da 0 (inclusive) à posição 7(exclusive)
print(primos[2:8])# da posição 2 à 8

# Fatiando e criando uma sublista
sub_primos = primos[1:5]
print(sub_primos)