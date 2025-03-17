# Objective = 
# Return true if subroot is part of root 
# A subtree is a a tree that consists of a node in tree and all of its node descendants 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def isSameTree(self, rootA, rootB):
        # Base case -> when both are none
        if not rootA and not rootB:
            return True
        # Handles when one of their values is different 
        if not rootA or not rootB or rootA.val != rootB.val:
            return False
    
        # Recursive call 
        return self.isSameTree(rootA.left, rootB.left) and self.isSameTree(rootA.right, rootB.right)
    
    def isSubtree(self, rootA, subroot):
        
        # NOTE = An empty tree is considered a subtree of any other tree!
        if not subroot:
            return True
        
        if not rootA:
            return False
        
        # Traverse through root A until we find an element with an equal root as subroot.
        # Ideal preorder traversal 
        
        # Start with root 
        # if rootA.val == subroot.val: check if they are the same
        if self.isSameTree(rootA, subroot):
            return True
        # Originally I had this like if rootA.val == subroot.val return self.isSameTree
        # This didn't work because we would return false when the root was [1,1] and subroot was [1]
        # It's not a subtree at the initial root, but it's a subtree at the root.left position. 
    
        return self.isSubtree(rootA.left, subroot) or self.isSubtree(rootA.right, subroot)
        
# Edge case [1,1] [1]
root = TreeNode(1)
root.left = TreeNode(1)

subroot = TreeNode(1)

        
# root = TreeNode(3)
# root.right = TreeNode(5)

# root.left = TreeNode(4)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.left.right.left = TreeNode(0)

# subroot = TreeNode(4)
# subroot.left = TreeNode(1)
# subroot.right = TreeNode(2)

print(root.isSubtree(root, subroot))