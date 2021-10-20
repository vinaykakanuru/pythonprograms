class BinarySearchTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    # adding a child node
    def add_child(self, val):
        # node already exist
        if val == self.data:
            return 

        # add element to left sub-tree
        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTree(val)
        
        # add element to right sub-tree
        if val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTree(val)

    # function to help seraching a node in given BST
    def search(self, val):
        if self.data == val:
            return True
        
        # search in left sub-tree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        # search in right sub-tree
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # In-order Traversal (Left, Root, Right)
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # pre-order traversal (Root, Left, Right)
    def pre_order_traversal(self):
        # adding Root element to an Array
        elements = [self.data]

        # adding Left sub-tree elements to an Array
        if self.left:
            elements += self.left.pre_order_traversal()
        
        # adding Right sub-tree elements to an Array
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements


    # post-order traversal (Left, Right, Root)
    def post_order_traversal(self):
        elements = []

        # adding Left sub-tree elements to an Array
        if self.left:
            elements += self.left.pre_order_traversal()
        
        # adding Right sub-tree elements to an Array
        if self.right:
            elements += self.right.pre_order_traversal()

        # adding Root element to an Array
        elements.append(self.data)
        
        return elements
    
    def find_min(self):
        # go towards to the last left Tree node 
        # (there'll be no left node to the extreme left node so returning self.data)
        if self.left is None:
            return self.data
        
        # recursive way to reach the extreme left node of a given BSTree
        return self.left.find_min()
    
    def find_max(self):
        # go towards to the last right Tree node 
        # (there'll be no Right node to the extreme Right node so returning self.data)
        if self.right is None:
            return self.data
        
        # recursive way to reach the extreme Right node of a given BSTree
        return self.right.find_max()


# Helper code to create a BST
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


# Driver code
countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = build_tree(countries)

print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

# Helper code to create a BST
root = BinarySearchTree(4)
root.left = BinarySearchTree(2)
root.right = BinarySearchTree(5)
root.left.left = BinarySearchTree(1)
root.left.right = BinarySearchTree(3)

# Driver code
print(root.in_order_traversal())
print(root.pre_order_traversal())
print(root.post_order_traversal())
print(root.find_min())
print(root.find_max())