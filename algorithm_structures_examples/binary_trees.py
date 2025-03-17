# Terminology =
# Tree size = Amount of nodes in the tree
# Tree height = Maximum number of edges from root node to leaf node. 
# Tree height VS. Tree depth =
# The height of a node is the number of edges on the longest path from a node to a leaf
# The depth of a node is the number of edges from the root to a node -> Root has a depth of 0 while each child is parent's depth + 1
# Example
# root = 10         -> height is 1, depth = 0
# root.left = 5     -> height is 0, depth = 1
# root.right = 15   -> height is 0, depth = 1


# Benefits =
# Fast access, insertion and deletion of nodes. 

# Types of trees =
# 1. Balanced = A tree is balanced when the height to the left and the height to the right have a difference of one or less. 
# Example = if the height to the left is 2 and right is 2 -> Balanced
# if the height to the left is 3 and right is 2 -> balanced because the difference is 1 
# if the height to the left is 2 and right is 4 -> Not balanced because the difference is more than 1
# 2. Complete = All levels before the last are completely filled and the last level is filled from left to right, no gaps. 
# 3. Full binary tree = it always have 0 or 2 children, never just 1 child
# 4. Perfect = means all nodes / children are on the same level. 

# Examples of common Binary trees =
# BST -> The root is always smaller than the right child and larger than left child. 
# Max heap -> Root is always the largest node
# Min Heap -> root is always the smallest node

# Implementation - EACH node can be linked to its left or right nodes. 

class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # Insert node 
    def insert(self, data):
        # Since root node can be None upon initialization we handle this case by just setting it 
        if self.data is None:
            self.data = data
            return
        
        if data < self.data:
            if self.left is None: 
                # Inserts node to the left
                self.left = TreeNode(data)
            else:
                # If there's a left node it recursively finds a left that is none to populate
                self.left.insert(data)
        else:
            if self.right is None: 
                # Inserts node to the right
                self.right = TreeNode(data)
            else: 
                # If there's a left node it recursively finds a left that is none to populate
                self.right.insert(data)
    
    # In order traversal -> useful for ordered binary trees 
    # Explores left -> node -> right. Starts at deepest left leaf node and goes up to root, then goes down right nodes 
    def TraverseOrder(self, root):
        res = []
        if root:
            res = self.TraverseOrder(root.left)
            res.append(root.data)
            # We use + to prevent appending a list, but extending the current list . 
            res =  res + self.TraverseOrder(root.right)
        return res
            
    # Pre order traversal -> copying a binary tree, common for decision trees and backtracking 
    # Explores node -> left -> right 
    def PreOrderTraverse(self, root):
        res = []
        if root:
            # Appends current node which is root 
            res.append(root.data)
            # Recursively 
            # Appends all left elements
            res = res + self.PreOrderTraverse(root.left)
            # Appends all right elements 
            res = res + self.PreOrderTraverse(root.right)
        return res

    # Post Order traversal -> Used to delete trees | Calculate height of a binary tree | Pruning trees when updates
    # Explores nodes left -> right -> root 
    def PostOrderTraversal(self, root):
        res = [ ]
        if root: 
            res = self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res 
    
    def DeleteNode(self, root, key):
        # When we don't find the node to delete
        if root is None: 
            return root 

        # Key is smaller than the root's data, traverse to the left
        if key < root.data:
            root.left = self.DeleteNode(root.left, key)
            
        # Traverse right     
        elif key > root.data:
            root.right = self.DeleteNode(root.right, key)
        
        # We traversed either right or left and key == root.data
        else: 
            # If it's a leaf node - No children, just remove node
            # This part is usually called in the self.DeleteNode(root.left) / self.DeleteNode(root.right) at the top and returns
            # None, as it returns none root.left = None / root.right = None -> Recursion 
            if root.left is None and root.right is None: 
                return None 
            
            # If node has a child, delete node and replace it with its single child 
            # If it doesn't have a left, we return its right 
            elif root.left is None: 
                return root.right
            # If it doesn't have a right, we return its left  
            elif root.right is None: 
                return root.left 
            
            # We find the in order sucessor, remember its the smallest leaf value to the right of the current node
            else: 
                successor = self.find_min(root.right)
                root.data = successor.data 
         
                root.right = self.DeleteNode(root.right, successor.data)
        return root 
    
    # This finds the inorder sucessor -> An inorder sucessor is the smallest value node on the right of the current node 
    def find_min(self, node):
        current = node 
        # We navigate until there's no more left and we reach the leaf node 
        while current.left is not None: 
            current = current.left
        return current 

    
root = TreeNode(10)
root.insert(8) 
root.insert(5)
root.insert(6)
root.insert(12)
root.insert(13)
# print(root.TraverseOrder(root))  
print(root.PreOrderTraverse(root))
root.DeleteNode(root, 6)
# print(root.PreOrderTraverse(root))


# Manual Insertion       
# root = TreeNode('R')
# nodeA = TreeNode('A')
# nodeB = TreeNode('B')
# nodeC = TreeNode('C')
# nodeD = TreeNode('D')
# nodeE = TreeNode('E')
# nodeF = TreeNode('F')
# nodeG = TreeNode('G')

# root.left = nodeA
# root.right = nodeB
# nodeA.left = nodeC
# nodeA.right = nodeD
# nodeB.left = nodeE
# nodeB.right = nodeF
# This makes the three balanced but not complete. 
# nodeC.left = nodeG

# Traversing a tree
# BFS => Nodes on the same level are visited before going to next level in trees. Sideways

# DFS => Down the tree to the leaf nodes. Downwards direction. 
# binT = TreeNode(5)
# binT.insert_node(4)
# binT.insert_node(3)
# binT.insert_node(2)
# binT.insert_node(6)
# binT.insert_node(7)
# print(binT.preOrderTraverse(binT))
# binT.delete_node(binT, 6)
# print(binT.preOrderTraverse(binT))

# print(binT.preOrderTraverse(binT))
# print(binT.inOrderTraverse(binT))
# print(binT.data)
# print(binT.left.data)
# print(binT.right.data)
# print(binT.findInorderSucessor(binT.right))
# print(binT.postOrderTraverse(binT))