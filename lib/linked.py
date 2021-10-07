"""
    Classe que representa cada unidade (elemento) da lista encadeada
    É dividida em duas partes:
    1) onde fica armazenada a informação relevante para o usuário (__data)
    2) O ponteiro para o próximo nodo da sequência (__next)
"""
class Node:

    def init(self, val):
        self.data = val     # Armazena a informação do usuário
        self.next = None  # Ponteiro para o próximo nodo (None = nenhum)

"""
    ESTRUTURA DE DADOS LISTA ENCADEADA
    A lista encadeada é uma estrutura de dados formada por unidades
    de informação chamadas nodos ou nós.
    Cada nodo da lista encadeada tem duas partes: uma, que armazena a
    informação e outra que guarda o endereço do próximo nodo da sequência
    A qualquer momento, temos um conhecimento apenas limitado de onde
    se encontram todos os nodos da lista. Sabemos apenas onde está o
    primeiro e o último nodo da sequência. Os nodos intermediários precisam
    ser encontrados partindo-se do primeiro e percorrendo a sequência
"""
class LinkedList:

    """
        Construtor da classe
    """

    def _init_(self):
        self.__head = None   # (cabeça)Ponteiro para o primeiro da lista
        self.__tail = None   # (Cauda) Ponteiro para o ultimo nodo da lista
        self.__count = 0     # Contador de nodos 

    """
        Método que informa se a lista esta ou não vazia
    """

    def is_empty(self):
        return self.__count == 0 

    def insert(self, pos, val):

        inserted = Node(val)

        # 1 caso: a lista está vazia 
        # O nodo criado será, ao mesmo tempo, o primeiro e o último

        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted

        self.__count += 1

        print(f"[Node] data: {inserted.data}, next: {inserted.next} ")

###############################################################

lista = LinkedList()

lista.insert(0, "1 kg batata")