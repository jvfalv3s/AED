import random
import time
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def __str__(self):
        return str(self.data)
        
class BinaryTree:
    def __init__(self, data = None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
            self.num_rotacoes = 0
            
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            inicio = time.time()
            self._insert_recursivamente(value, self.root)
            fim = time.time()
            tempo_insercao = fim - inicio
            print("Tempo de inserção:\n", tempo_insercao)
    
    def _insert_recursivamente(self, value, node):
        if value == node.data:
            return # Não insere chaves repetidas
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursivamente(value, node.left)
                self.num_rotacoes += 1
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursivamente(value, node.right)
                self.num_rotacoes += 1
            
    def inserir_aleatoriamente(self, num):
        import random
        for i in range(num):
            value = random.randint(1, 20)  # Gera números aleatórios entre 1 e 20
            self.insert(value)
            
    def imprimir(self):
        if self.root:
            self._imprimir_recursivamente(self.root)

    def _imprimir_recursivamente(self, node):
        if node:
            self._imprimir_recursivamente(node.left)
            print(node)
            self._imprimir_recursivamente(node.right)
            


def preparar_conjunto(tipo, tamanho):
        if tipo == 'A':
            return list(range(1, tamanho + 1))  # Chaves por ordem crescente
        elif tipo == 'B':
            return list(range(tamanho, 0, -1))  # Chaves por ordem decrescente
        elif tipo == 'C':
            return random.sample(range(1, tamanho * 10), tamanho)  # Chaves aleatórias
        elif tipo == 'D':
            repetidos = int(0.9 * tamanho)  # 90% de repetições
            nao_repetidos = tamanho - repetidos
            chaves_repetidas = random.choices(range(1, tamanho * 10), k=repetidos)
            chaves_nao_repetidas = random.sample(range(tamanho * 10, tamanho * 100), nao_repetidos)
            return chaves_repetidas + chaves_nao_repetidas
        else:
            return []

# Exemplo de uso
arvore = BinaryTree()
arvore.inserir_aleatoriamente(20)  # Insere 20 nós com valores aleatórios entre 1 e 20

print("Árvore Binária\n")
print("Impressão em ordem:")
arvore.imprimir()


tamanho_conjunto = 20  # Tamanho do conjunto de chaves
conjunto_A = preparar_conjunto('A', tamanho_conjunto)
conjunto_B = preparar_conjunto('B', tamanho_conjunto)
conjunto_C = preparar_conjunto('C', tamanho_conjunto)
conjunto_D = preparar_conjunto('D', tamanho_conjunto)

print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)
print("Conjunto C:", conjunto_C)
print("Conjunto D:", conjunto_D)