print("arvore binaria de busca/pesquisa")

from arvoreBinaria import Node

class BinarySearchTree:
    def __init__(self, data = None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
            
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value > x.data:
                x = x.right
            else:
                x = x.left
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
            
    def search(self, value, node = 0):
        if node == 0:
            node = self.root
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)