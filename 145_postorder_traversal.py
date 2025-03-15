class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data 
        self.left = left
        self.right = right
    
    # left - right - root
    def postorderTraversal(self, root):
        res = []
        if root:
            res =  self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res
            
tree = TreeNode()
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(tree.postorderTraversal(tree))
        
