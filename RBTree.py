import sys

from RBNode import RBNode


class RBTree():
    def __init__(tree):
        tree.leafNil = RBNode('NIL')
        tree.leafNil.color = 'b'  # nil is black
        tree.leafNil.left = None
        tree.leafNil.right = None
        tree.root = tree.leafNil  # changed later after insertion

    def search(tree, node, searchWord):
        if node.word.casefold() == searchWord.casefold() or node == tree.leafNil:
            return node

        if searchWord.casefold() < node.word.casefold():
            return tree.search(node.left, searchWord)
        return tree.search(node.right, searchWord)

    def totalNodes(tree, currentNode):
        if currentNode == tree.leafNil:
            return 0
        else:
            return 1 + tree.totalNodes(currentNode.left) + tree.totalNodes(currentNode.right)

    def height(tree, currentNode):
        if currentNode == tree.leafNil:
            return -1
        else:
            return 1 + max(tree.height(currentNode.left), tree.height(currentNode.right))

    def insert(tree, word):
        # Ordinary Binary Search Insertion
        new_node = RBNode(word)
        new_node.parent = None
        new_node.left = tree.leafNil
        new_node.right = tree.leafNil
        new_node.red = 'r'  # new node is always red

        parent = None
        current = tree.root
        # reaching correct position
        while current != tree.leafNil:
            parent = current
            if new_node.word.casefold() < current.word.casefold():
                current = current.left
            elif new_node.word.casefold() > current.word.casefold():
                current = current.right
            else:
                return -1  # word already exists

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:  # empty tree
            tree.root = new_node
        # decide whether left or right child
        elif new_node.word.casefold() < parent.word.casefold():
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        tree.fixinsert(new_node)

    def printinorder(tree, node):
        if node != tree.leafNil:
            tree.printinorder(node.left)
            sys.stdout.write(node.word + "," + node.color + "    ")
            tree.printinorder(node.right)

    def left_rotate(tree, current):
        rightchild = current.right
        current.right = rightchild.left  # set right subtree of current to left subtree of right child
        if rightchild.left != tree.leafNil:  # check if subtree exists
            rightchild.left.parent = current  # resetting parent of the subtree
        rightchild.parent = current.parent  # connect the right child with grandparent
        if current.parent is None:  # current was root
            tree.root = rightchild  # update root
        elif current == current.parent.left:  # current was left child for its parent
            current.parent.left = rightchild  # update left of parent to be right child
        else:  # current was right child for its parent
            current.parent.right = rightchild  # update right of parent to be right child
        rightchild.left = current
        current.parent = rightchild

    def right_rotate(tree, current):
        leftchild = current.left
        current.left = leftchild.right  # set left subtree of current to right subtree of left child
        if leftchild.right != tree.leafNil:  # check if subtree exists
            leftchild.right.parent = current  # resetting parent of the subtree
        leftchild.parent = current.parent  # connect the left child with grandparent
        if current.parent is None:  # current was root
            tree.root = leftchild  # update root
        elif current == current.parent.right:  # current was right of parent
            current.parent.right = leftchild  # update right of parent to be right child
        else:  # current was left of parent
            current.parent.left = leftchild  # update left of parent to be left child
        leftchild.right = current
        current.parent = leftchild

    def fixinsert(tree, node):
        if node != tree.root:  # because we test for parent
            while node.parent.parent is not None and node.parent.color == 'r':
                if node.parent == node.parent.parent.left:  # parent is left
                    uncle = node.parent.parent.right  # uncle is opposite to parent
                    if uncle.color == 'b':
                        if node == node.parent.right:  # check if left right to make it left left
                            node = node.parent
                            tree.left_rotate(node)  # it is left right, rotate to make left left
                        node.parent.color = 'b'  # switch colors
                        node.parent.parent.color = 'r'
                        tree.right_rotate(node.parent.parent)
                else:  # parent is right
                    uncle = node.parent.parent.left  # uncle is opposite
                    if uncle.color == 'b':
                        if node == node.parent.left:  # check if right left to make it right right
                            node = node.parent
                            tree.right_rotate(node)  # it is right left, make right right
                        node.parent.color = 'b'  # switch colors
                        node.parent.parent.color = 'r'
                        tree.left_rotate(node.parent.parent)
                if uncle.color == 'r':  # change colors of uncle, parent and grand
                    uncle.color = 'b'
                    node.parent.color = 'b'
                    uncle.parent.color = 'r'
                    node = uncle.parent  # input grand as the new node
                if node == tree.root:
                    break
            tree.root.color = 'b'
