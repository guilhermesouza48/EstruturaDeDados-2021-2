# Importar o valor da constate pi
# math é o nome da biblioteca onde pi se encontra
from math import pi

# Função é um trecho de código que tem um  nome e pode
# receber informações externas para fazer seu trabalho.
# Opcionalmente, uma função pode também produzir um valor
# de resultado
# Uma função é deinida apenas uma vez e pode ser utilizada
# (Chamada) várias vezes, evitando repetições de código.
# Existem funções  já providos pela linguagem, como, por exemplo:
# len(), range() e sort(), e podemos definir também nossas próprias funções.

def imc(peso, altura): # Definição (ou declaração) da função
    return peso / altura ** 2

    # Trechos entre aspas triplas são um tipo especial de comentário
    # chamado docstring , e servem para documentar
    #o propósito de uma função ou classe.
     #peso / (altura)² 

# float(): converte o valor informado em um número com casas decimais
# (floating point)

p =  float(input("Informe o peso da pessoa:"))
a = float(input("Informe a altura da pessoa:"))

# Fazendo uma chamada à função imc()
resultado = imc (p, a)

print(f"O IMC calculado é {resultado}.")

def area_forma(base, altura, forma = "R"):
# Funções que calcula a área de uma das seuintes formas geométricas:
# retângulo, triângulo ou elipse
# Parâmetro forma:
# "R" == retângulo  (parâmetro opcional com valor padrão)
# "T" == triângulo
# "E" == elipse

    area = 0
    if forma == "R":   
        area = base * altura
    elif forma == "T":
        area = base * altura / 2
    elif forma == "E":
        area = ( base / 2 ) * ( altura / 2 ) * pi
    return area

print('--------------------//------------------')

print(f"Retângulo 7.5X11:{area_forma(7.5, 11, 'R')}")
print(f"Triângulo 8X12:{area_forma(8, 12, 'T')}")
print(f"Circulo 15X15:{area_forma(15, 15, 'E')}")
print(f"Quadrado 9.5X9.5:{area_forma(9.5, 9.5)}")