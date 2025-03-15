class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data 
        self.left = left
        self.right = right
        
    # left, root, right
    def inOrderTraverse(self, root):
        res = []
        if root:
            res = self.inOrderTraverse(root.left)
            res.append(root.data)
            res = res + self.inOrderTraverse(root.right)
        return res      
    
    def reverseTree(self, root):
        # preorder traversal 
        # Starts root 
        # Switch left - right
        prev_right = root.right
        root.right = root.left
        root.left = prev_right
        
        # Move left of root
        # Switch left - right as traverse left 
        if root.left:
            root.left = self.reverseTree(root.left)
        
        # Move right of root 
        # Switch left - right as traverse right
        if root.right:
            root.right = self.reverseTree(root.right)
        
        return root
        
        
        
tree = TreeNode(4)

tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)

tree.right = TreeNode(7)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)
print(tree.inOrderTraverse(tree))
tree.reverseTree(tree)
print(tree.inOrderTraverse(tree))


# Traverse left -> reverse elements 
# prev_right = tree.right
# tree.right = tree.left
# tree.left = prev_right

# If it's a leaf node -> Go back to prev node 
# If node has left not right 

# Objective = Given root of bin tree, invert it and return its root 
# Example 

