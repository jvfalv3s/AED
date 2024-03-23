#codigo de implementação de uma arvore binaria simples.

print("Arvore Binaria")

class Node: #classe nó
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def __str__(self):
        return str(self.data)
        
class BinaryTree:  #classe arvore binaria
    def __init__(self, data = None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
            
    def insert(self, value):
        #inserção de um novo nó na arvore binaria
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insertRecursivamente(self, value, node): #tentativa de inserção recursiva
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
            
    def inserRandom(self, num): #inserção de valores aleatorios
        for i in range(num):
            self.insert(i)
            
    def imprimir(self): #impressão da arvore binaria
        if self.root:
            self._imprimir(self.root)

    def _imprimirRecursivamente(self, node): #tentativa de impressão recursiva
        if node is None:
            self._imprimirRecursivamente(node.left)
            print(node)
            self._imprimirRecursivamente(node.right)