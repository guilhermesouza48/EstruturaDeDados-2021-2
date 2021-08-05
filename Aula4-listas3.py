# Listas de strings 

Frutas = ["laranja","maçã","uva","pera","mamão","abacate","amora"]

print('-------------------//--------------------')

# Imprimindo apenas a fruta "uva"

print(Frutas[2])

print('-------------------//--------------------')

# Substituindo "pera" por "melão"

Frutas[3] = "melão"
print(Frutas)

print('-------------------//--------------------')

# Descobrindo quantos elementos há na lista

print(len(Frutas))

print('-------------------//--------------------')

# Percorrendo e imprimindo cada um dos elementos da lista

for fruta in Frutas:
    print(fruta)

print('-------------------//--------------------')

# Percorrendo e imprimindo cada elemento e sua posição

for i in range(len(Frutas)):
    print(f"{Frutas[i]} está na posição {i}")

print('-------------------//--------------------')

# Percurso em ordem invertida
# 1º Argumento: len(Frutas) -1: a lista precisa começar na último elemento, que é
# determinado por len() - 1
# 2º Argumento: -1, porque o limite final não entra e precisamos terminar em 0
# 3º Argumento: -1,  porque a  lista precisa ser decrescente

for p in range(len(Frutas)-1, -1, -1):
    print(Frutas[p])

print('-------------------//--------------------')

# Ordenando o vetor em ordem alfabética 

frutas.sort()
print(frutas)