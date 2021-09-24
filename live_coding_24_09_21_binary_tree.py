class Tree:
    def __init__(self):
        self.root = None


    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True


    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)


    def max_value(self):
        pass

    def min_value(self):
        pass

    def delete(self,value):
        pass



    def print_the_tree(self):
        self._print_the_tree(self.root)


    # separation for recursion
    def _print_the_tree(self, current_node):
        print(current_node.value)

        if current_node.left is not None:
            self._print_the_tree(current_node.left)

        if current_node.right is not None:
            self._print_the_tree(current_node.right)



#    def _insert_with_search(self, value):
#        found_node = self._search(self.root, value)

        # 2 scenarios
        # s
        #found_node.parent

    def _insert(self, current_node,value):

        if (value > current_node.value):
            #add leaf is absent
            #add to the right
            if current_node.right is None:
                current_node.right = Node (value, current_node)
                return
            return self._insert(current_node.right,value)
        else:
            # add to the lest
            if current_node.left is None:
                current_node.left= Node (value, current_node)
                return
            return self._insert(current_node.left,value)


    def _search(self, node_to_check, value):


        #no more nodes, our father is a leaf
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check
        # value = 15
        # node_to_check= 15

        # value = 8
        # node_to_check = 6
        if value > self.root.value:
            # go right
           return self._search(node_to_check.right,value)
        else:
            # go left
           return self._search(node_to_check.left,value)


class Node:
    def __init__(self,value, parent = None,right= None,left= None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value

tree= Tree()

tree.insert(11)
tree.insert(10)
tree.insert(8)
tree.insert(6)
tree.insert(5)


print(tree.search(11))
print(tree.search(10))
print(tree.search(8))
print(tree.search(6))
print(tree.search(5))

tree.print_the_tree()
