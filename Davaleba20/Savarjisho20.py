

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node
    
    #davalebis metodi
    def print_leaf_nodes(self):
        leafs = []
        self._print_leaf_nodes(self.root, leafs)
        print(leafs)

    def _print_leaf_nodes(self, node, leafs):
        if node is not None:
            if node.left is None and node.right is None:
                leafs.append(node.key)
            else:
                self._print_leaf_nodes(node.left, leafs)
                self._print_leaf_nodes(node.right, leafs)
        
    def count_edges(self):
        count = []
        self._count_edges(self.root, count)
        print(f"The tree has {len(count)} edges")

    def _count_edges(self, node, count):
        if node is not None:
            if node.left is not None and node.right is not None:
                count.append(1)
                count.append(1)
                self._count_edges(node.left, count)
                self._count_edges(node.right, count)
            elif node.left is not None and node.right is None:
                count.append(1)
                self._count_edges(node.left, count)
            elif node.left is None and node.right is not None:
                count.append(1)
                self._count_edges(node.right, count)
        

        
            

    def printParent(self):
        print("Printing Parent Tree")
        self._printParent(self.root, None)

    def _printParent(self, node, parent):
        if node is not None:
            if parent is None:
                print(node.key, " -> Root")
            else:
                print(node.key, " -> ", parent.key)

            self._printParent(node.left, node)
            self._printParent(node.right, node)


binary_tree = BinaryTree()
binary_tree.insert(10)
binary_tree.insert(7)
binary_tree.insert(8)
binary_tree.insert(11)
binary_tree.insert(25)
binary_tree.insert(14)
binary_tree.insert(2)

binary_tree.printParent()

binary_tree.print_leaf_nodes()
binary_tree.count_edges()