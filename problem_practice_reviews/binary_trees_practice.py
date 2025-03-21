class TreeNode: 
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    # Insert elements to a binary tree following the left - root - right structure.     
    def insertNode(self, val): 
        # Determine if the root doesn't exist 
        if self.data is None: 
            self.data = val
        
        # Determine if the newly added el is less or higher than root 
        if val < self.data: 
            # If left doesn't exist we add the new node
            if self.left is None: 
                self.left = TreeNode(val)
            # If it exists, we use recursion to search again of the lowest element to left 
            else: 
                self.left.insertNode(val)
        else: 
            if self.right is None: 
                self.right = TreeNode(val)
            else: 
                self.right.insertNode(val)
    
    # In order traverse : left - root - right
    def inOrderTraverse(self, node):
        res = []
        if node:
            res = self.inOrderTraverse(node.left)
            res.append(node.data)
            res = res + self.inOrderTraverse(node.right)
        return res 
    
    # Pre Order traverse : root - left - right
    def preOrderTraverse(self, node): 
        res = []
        if node: 
            res.append(node.data)
            res = res + self.preOrderTraverse(node.left)
            res = res + self.preOrderTraverse(node.right)
        return res
    # Post Order traverse : left - right - root
    
    def postOrderTraverse(self, node): 
        res = []
        if node: 
            
            res = self.postOrderTraverse(node.left)
            res = res + self.postOrderTraverse(node.right)
            res.append(node.data)      
        return res  
    
    # Remember in order sucessors are the smallest element to the left on the right of the current node
    def findInOrderSucessor(self, node):
        current = node 
        
        while current.left: 
            current = current.left
        return current
    
# Inverting binary tree
def invertBinaryTree(root):
    
    # Check if the root has a value
    if root is None: 
        return None
    
    # Swap left and right
    prevLeft = root.left
    root.left = root.right
    root.right = prevLeft
    
    # Handles recursion and moves to left or right
    if root.left: 
        root.left = invertBinaryTree(root.left)
    elif root.right: 
        root.right = invertBinaryTree(root.right)
        
    return root 

# Depth of binary tree is the number of nodes from root to leaf 
def calculateTreeDepth(root):
    # Base case  
    if root is None: 
        return 0
    
    # Find leaf node amount to the left 
    left = calculateTreeDepth(root.left)
    # Find leaf node right 
    right = calculateTreeDepth(root.right)
    
    # Determine which is the max from both of them
    return max(left, right) + 1

# Test tree for calculating depth 
# tree = TreeNode(3)

# tree.left = TreeNode(9)

# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)


# The length of the longest path between any two nodes 
def calculateDiameter(root):
    # Non local bariably to calculate diameter inside dfs function
    diameter = 0 
    def dfs(root): 
        # Base case, gets returned when it's a leaf node
        if root is None: 
            return 0 
        
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        # Set the diameter to its max, by adding current left and right 
        nonlocal diameter
        diameter = max(diameter, left + right)
        
        # Returns the result of the depth 
        return max(left, right) + 1 
    # Function call
    dfs(root)
    # nonlocal variable return and res 
    return diameter
        
        
        # Diameter is the sum of left and right. 
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right =  TreeNode(3)
print(calculateDiameter(tree))


# Test tree data for invert binary tree
# tree = TreeNode(4)
# tree.left = TreeNode(2)
# tree.left.left = TreeNode(1)
# tree.left.right = TreeNode(3)

# tree.right = TreeNode(7)
# tree.right.left = TreeNode(6)
# tree.right.right = TreeNode(9)
