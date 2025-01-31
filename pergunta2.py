class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def caminho(root, key):
        def caminho_helper(node, key, path):
            if node is None:
                return False
            path.append(node.value)
            if node.value == key:
                return True
            if (node.left and caminho_helper(node.left, key, path)) or (node.right and caminho_helper(node.right, key, path)):
                return True
            path.pop()
            return False

        path = []
        if caminho_helper(root, key, path):
            return " -> ".join(path)
        else:
            return "Palavra não encontrada"
    
root = Node("Maça")
root.left = Node("Morango")
root.left.left = Node("Goiaba")
root.left.right = Node("Limão")
root.right = Node("Pera")
root.right.right = Node("Abacaxi")
root.right.right.right = Node("Laranja")
root.right.right.right.left = Node("Banana")
root.right.right.right.right = Node("Cebola")

fruta = input("Qual fruta quer encontrar? ")

print(caminho(root, fruta))