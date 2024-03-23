#codigo de implementação de uma arvore binaria simples.

print("Arvore Binaria")

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
            
if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)