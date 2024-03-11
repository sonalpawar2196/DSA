class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.__insert_helper(self.root, new_node)
    def _inorder_traversal(self, current):
        if current is not None:
            self._inorder_traversal(current.left)
            print(current.data, end= " ")
            self._inorder_traversal(current.right)
    def _pre_order_traversal(self, current):
        if current is not None:
            print(current.data, end=" ")
            self._pre_order_traversal(current.left)
            self._pre_order_traversal(current.right)
    def _post_order_traversal(self, current):
        if current is not None:
            self._post_order_traversal(current.left)
            self._post_order_traversal(current.right)
            print(current.data, end=" ")
            
    def __insert_helper(self, current, new_node):
        if new_node.data <= current.data:
            if current.left is None:
                current.left = new_node
            else: 
                self.__insert_helper(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.__insert_helper(current.right, new_node)
    
    def print_tree(self):
        if self.root is not None:
            print("in order traversal ")
            self._inorder_traversal(self.root)
            print()
            
            print("pre order traversal ")
            self._pre_order_traversal(self.root)
            print()

            print("post order traversal ")
            self._post_order_traversal(self.root)
            print()
        
            
tree = BinaryTree(None)
tree.insert(50)
tree.insert(25)
tree.insert(12)
tree.insert(15)
tree.insert(60)
tree.insert(55)
tree.insert(65)

print("In-order traversal:", end=" ")
tree.print_tree()