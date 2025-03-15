class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data 
        self.left = left
        self.right = right
    
    # Left - root - right
    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
            
tree = TreeNode()
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(tree.inOrderTraversal(tree))
        

