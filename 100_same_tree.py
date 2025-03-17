# Objective  = Check if two trees have the same structure and same value. 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
    
    def isSameTree(self, p, q):
        # Base case
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
    
# tree1 = TreeNode(1)
# tree1.left = TreeNode(2)
# tree1.right = TreeNode(3)

# tree2 = TreeNode(1)
# tree2.left = TreeNode(2)
# tree2.right = TreeNode(3)

tree1 = TreeNode(2)

tree1.left = TreeNode(2)
tree1.left.right = TreeNode(2)
tree1.left.right.left = TreeNode(2)
tree1.right = TreeNode(2)

tree2 = TreeNode(2)
tree2.left = TreeNode(2)
tree2.left.left = TreeNode(2)
tree2.right = TreeNode(2)
tree2.right.left = TreeNode(2)


print(tree1.isSameTree(tree1, tree2))
