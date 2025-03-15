class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data 
        self.left = left
        self.right = right
    
    # root - left - right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
            
tree = TreeNode()
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(tree.preorderTraversal(tree))
        
