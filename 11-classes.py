# Classe é uma estrutura que representa conjuntamente
# dados e algoritmos. Uma classe é como uma "forma de bolo"
# com a qual podemos criar diferentes "bolos" (objetos).
# Cada "bolo" (objeto) pode ser feito com seus próprios
# ingredientes (dados) e modos de fazer (algoritmos), mas
# terão sempre o formato determinado pela "forma" (classe).

class FormaGeometrica():

    # Dados
    # Quando pertence a uma classe, ganham o nome de
    # ATRIBUTOS
    # base = 0
    # altura = 0
    # tipo = "R"  # Retângulo

    # Algoritmos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham o nome de MÉTODOS

    # Este método é executado quando um objeto é criado a partir
    # de uma classe (construtor)
    def _init_(self, base, altura, tipo = "R"):
        # Recebe os valores passados ao construtor e os armazena
        # dentro dos atributos

        #print(f"base: {base} ({type(base)}), altura: {altura} ({type(altura)})")

        if type(base) not in [int, float] or base <= 0:
            raise Exception("A base deve ser numérica e maior que zero.")
        elif type(altura) not in [int, float] or altura <= 0:
            raise Exception("A altura deve ser numérica e maior que zero.")
        elif tipo not in["R", "T", "E"]:
            raise Exception("O tipo deve ser R, T ou E.")


        # Ajustando o valor dos atributos privados
        self.__base = base
        self.__altura = altura
        self.__tipo = tipo

    # Getter é um método que possibilita saber o valor de um atributo
    # privado do lado de fora da classe
    def get_base(self):
        return self.__base

    # Setter é um método que possibilita alterar o valor de um atributo
    # privado inclusive do lado de fora da classe
    def set_base(self, valor):
        if type(valor) not in  [int, float] or valor <=0 :
            raise Exception("* A base deve ser númerica e maior que zero.")

        self.__base = valor

################################################################

# Criando objetos (instanciando) a partir da classe
retangulo1 = FormaGeometrica(15, 10, "R")   # Chama o _init_
triangulo1 = FormaGeometrica(6.4, 9, "T")

#retangulo1.__base = 5
retangulo1.set_base(9.6)

# retangulo1.__base = 0
# triangulo1.__tipo = "Yadayada"

#problematico = FormaGeometrica(7.2, 5.4, "T")

print(f"[retangulo1] base: {retangulo1.get_base()}")

#print(f"[retangulo1] base: {retangulo1._base}, altura: {retangulo1.altura}, tipo: {retangulo1._tipo}")

#print(f"[triangulo1] base: {triangulo1._base}, altura: {triangulo1.altura}, tipo: {triangulo1._tipo}")