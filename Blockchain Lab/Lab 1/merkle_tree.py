import hashlib

class Tree:
    
    def __init__(self, hashes, value, root, left=None, right=None):
        self.root = root
        self.value = value
        self.left = left
        self.right = right
        
    def create_tree(hashes, value):
        if len(hashes) == 1:
            return Tree(hashes[0], value[0], hashes[0])
        else:
            return Tree(None, value, hash_value("".join(hashes)), create_tree(hashes[:len(hashes)//2], value[:len(value)//2]), create_tree(hashes[len(hashes)//2:], value[len(value)//2:]))
        
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        return print(self.value, self.root)
        if self.right:
            self.right.print_tree()
        
def hash_value(value):
    # return hashlib.sha256(value.encode()).hexdigest()
    return value

num = int(input("Enter the number of transactions: "))
values = []
hashes = []
for i in range(num):
    transaction = input("Enter the transaction: ")
    values.append(transaction)
    hashes.append(hash_value(transaction))

tree = Tree(hashes, values, hash_value("".join(hashes)))

tree.print_tree()