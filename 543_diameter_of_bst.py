# Objective = return the length of the diameter of the tree
# Diameter is the length of the longest path between any two nodes in a tree 
# Length is the number of edges between two nodes 

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
    def diameterOfBinTree(self, root):
        # Store diameter in a variable 
        self.diameter = 0
        def dfs(curr):
            # If we reach a leaf node we return 0 
            if not curr: 
                return 0 
            
            # We do a post order traversal so we run the function over the left and right side 
            left = dfs(curr.left)
            right = dfs(curr.right)   
            
            # We calculate the diameter with the current left and right 
            self.diameter = max(self.diameter, left + right)
            
            # This calculates the height
            return 1 + max(left, right)
        dfs(root)
        return self.diameter
    
tree = TreeNode(3)

# tree.right = TreeNode(3)

tree.left = TreeNode(1)
# tree.left.left = TreeNode(4)
tree.left.right = TreeNode(2)
print(tree.postOrderTraverse(tree))