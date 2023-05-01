class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Insert something into the tree.
    def insert(self, val):
        #if self.val is None:
            #self.val = val

        if val < self.val:  # if less than
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:  # if greater than
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    # Check if a value is in the tree.
    def contains(self, val):
        if val == self.val:
            return True

        if val < self.val:  # if less than
            if self.left is None:
                return False
            else:
                return self.left.contains(val)
        else:  # if greater than
            if self.right is None:
                return False
            else:
                return self.right.contains(val)

    # Return all the items in the tree as a sorted list.
    def toList(self):
        lst = []
        # go through left
        if self.left:
            lst += self.left.toList()

        # add self.val
        lst.append(self.val)

        # go through right
        if self.right:
            lst += self.right.toList()

        return lst

    def biggest(self):
        if self.right:
            return self.right.biggest()
        else:
            return self.val

    def depth(self):
        if self.left and self.right:
            return max(self.right.depth(), self.left.depth()) + 1
        elif self.right:
            return self.right.depth() + 1
        elif self.left:
            return self.left.depth() + 1
        else:
            return 0

class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class.
    def __init__(self):
        self.root = None

    # Insert something into the tree.
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert(val)

    # Check if a value is in the tree.
    def contains(self, val):
        if self.root is None:
            return False
        else:
            return self.root.contains(val)

    # Return all the items in the tree as a sorted list.
    def toList(self):
        if self.root is None:
            return []
        else:
            return self.root.toList()

    def biggest(self):
        if self.root is None:
            return 0
        else:
            return self.root.biggest()

    def depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.depth()

def main():
    #s = input("Enter a list of numbers, seperated by spaces: ")
    #lst = s.split()

    lst = {32, 52, 1, 2, 6, 90, 23213, 35, 9, 7, 8}

    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))

    print(tree.contains(5))
    print(tree.toList())
    print(tree.biggest())
    print(tree.depth())


if __name__ == "__main__":
    main()