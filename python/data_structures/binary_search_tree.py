from data_structures.binary_tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):
    def add(self, value):
        def move(root, new_node):
            if not root:
                return
            if new_node.value < root.value:
                if root.left:
                    move(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    move(root.right, new_node)
                else:
                    root.right = new_node

        added_node = Node(value)
        if not self.root:
            self.root = added_node
            return
        move(self.root, added_node)

