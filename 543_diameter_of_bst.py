# Objective = return the length of the diameter of the tree
# Diameter is the length of the longest path between any two nodes in a tree 
# Length is the number of edges between two nodes 

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    # Neetcode solution
    def diameterOfBinTree(self, root):
        # Variable that stores the diameter
        self.res = 0 
        
        # Returns the max height 
        def dfs(curr):
            if not curr:
                return 0 
            # Max depth to left
            left = dfs(curr.left)
            # Max depth to right
            right = dfs(curr.right)
            
            # We add the two and set it to the diameter
            self.res = max(self.res, left + right)
            # keeps hold of diameter
            return 1 + max(left, right)
        dfs(root)
        return self.res 
    
    
tree = TreeNode(3)

# tree.right = TreeNode(3)

tree.left = TreeNode(1)
# tree.left.left = TreeNode(4)
tree.left.right = TreeNode(2)
print(tree.postOrderTraverse(tree))