#codigo de implementação de uma arvore binaria simples.

print("Arvore Binaria")

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Inserção de um novo nó com dados

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

# Busca de um nó com dados

def search(root, data):
    if root is None or root.data == data:
        return root
    if root.data < data:
        return search(root.right, data)
    return search(root.left, data)

# Impressão em ordem

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
        
# Impressão em pré-ordem

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
        
        
# Impressão em pós-ordem

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
        
# Teste

root = Node(10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 18)

print("Inorder")

inorder(root)

print("Preorder")

preorder(root)

print("Postorder")

postorder(root)

print("Busca")

print(search(root, 8).data)

print(search(root, 17))

print(search(root, 18).data)

print(search(root, 10).data)

print(search(root, 5).data)

# Fim do código