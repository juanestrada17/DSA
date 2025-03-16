class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # Very similar solution to 543 diamater of bst, but instead of calculating the diameter we find the max difference between 
    # All depths of the bst 
    def isBalanced(self, root):
        self.res = 0 
        def dfs(curr): 
            if curr is None: 
                return 0 
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # When calculating the diameter we do right + left, here we just calc the difference 
            self.res = max(self.res, abs(right - left))
            
            return 1 + max(left, right)
        dfs(root)
        return False if self.res > 1 else True
    
    def isBalancedAlter(self, root) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        
        
    
# tree = TreeNode(3)

# tree.left = TreeNode(9)

# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)
# print(tree.isBalanced(tree))

####

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)

tree.left.left = TreeNode(3)
tree.left.left.left = TreeNode(4)
tree.left.left.right = TreeNode(4)

tree.left.right = TreeNode(3)
print(tree.isBalanced(tree))



# Determine if a tree is height balanced -> The depth never differs by more than 1 
