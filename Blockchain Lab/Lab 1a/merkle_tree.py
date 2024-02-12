import hashlib

class Node:
    def __init__(self, hash_value, value=None, left=None, right=None):
        self.hash_value = hash_value
        self.value = value
        self.left = left
        self.right = right
        
def create_merkle_tree(hashes, values):
    if len(hashes) == 1:
        return Node(hashes[0], values[0])
    else:
        return Node(hashlib.sha256("".join(hashes).encode()).hexdigest(), values, create_merkle_tree(hashes[:len(hashes)//2], values[:len(values)//2]), create_merkle_tree(hashes[len(hashes)//2:], values[len(values)//2:]))
        
def print_merkle_tree(tree):
    if tree.left:
        print_merkle_tree(tree.left)
    if tree.right:
        print_merkle_tree(tree.right)
    print("Hash value:",tree.hash_value, "Transactions:", tree.value)


number_of_transactions = int(input("Enter the number of transactions: "))

transactions = []
hashes = []

for i in range(number_of_transactions):
    transaction = input("Enter the transaction: ")
    transactions.append(transaction)
    hashes.append(hashlib.sha256(transaction.encode()).hexdigest())
    
if len(transactions) % 2 != 0:
    transactions.append(transactions[-1])
    hashes.append(hashes[-1])
    
merkle_tree = create_merkle_tree(hashes, transactions)

print_merkle_tree(merkle_tree)