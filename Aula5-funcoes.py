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