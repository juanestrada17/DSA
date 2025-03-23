class TreeNode: 
    def __init__(self,data=None, left=None, right=None):
        self.data = data 
        self.left = left
        self.right = right
        
    # Traversing over trees 
    # In order -> left - root - right
    def inOrderTraverse(self, root):
        # We store the values in order in an list
        res = []
        if root:
            # root.left is 4 -> now it doesn't have a left and 4 is the root
            res = self.inOrderTraverse(root.left) 
            # Since now 4 is the root we append it to the res. We can also just make it a void function that just prints them
            res.append(root.data)
            # Same procedure with right, however we make sure we extend res so that we don't append a lest to a list 
            res = res + self.inOrderTraverse(root.right)
        # Returns the list, we can also just print them 
        return res 
    
    # Pre order -> root - left - right 
    def preOrderTraverse(self, root): 
        res = []
        if root: 
            res.append(root.data)
            res = res + self.preOrderTraverse(root.left)
            res = res + self.preOrderTraverse(root.righ)
        return res 
        
    # Post order -> left - right - root 
    def postOrderTraverse(self, root):
        res = []
        if root: 
            res = self.postOrderTraverse(root.left)
            res = res + self.postOrderTraverse(root.right)
            res.append(root.data)
        return res 
    
    # Inserting to a binary tree where we follow its left < root < right structure 
    def insertNode(self, newNode):
        # We check if we have a root node first  
        if not self.data: 
            # Set the root to be the new node 
            self.data = newNode       
        # If the new value is lower than current root, it means it goes to the left
        if newNode < self.data: 
            # We check if it already has a left before inserting 
            if self.left: 
                # If it has a left we do recursion on the left side until we find no self.left 
                self.left.insertNode(newNode)
            else:
                self.left = TreeNode(newNode)
        else:
            if self.right: 
                self.right.insertNode(newNode)
            else: 
                self.right = TreeNode(newNode)
                
        # Deleting a node in a well structured binary tree means =>
        # If the node is a leaf it's just deleted 
        # If the node is a parent with only one children, we switch parent with only child and delete child
        # If the node is a parent with two children, we switch the parent with the in order sucessor. Then delete the node  
        
        # Finding the in order sucessor is useful for this case- method is 
    def findInOrderSucessor(self, node):
        # Finding the in order sucessor means. The left-most element of the right branch
        # When we call this method we would call it over tree.findInOrderSucessor(tree.right)
        tempNode = node 
        while tempNode: 
            tempNode = tempNode.left
        return tempNode
    
    def reverseBinaryTree(self, root):
        # Since its a recursive function we need to have a base case
        if root is None: 
            return None
        
        # The logic to reverse it is:
        prevLeft = root.left 
        root.left = root.right
        root.right = prevLeft
        
        # We need to use recursion so we do post order traverse 
        root.left = self.reverseBinaryTree(root.left)
        root.right = self.reverseBinaryTree(root.right)
        
        return root 

    # When solving binary tree problems. It's commonly useful to know the tree depth and the height
    # The depth represents how deep is a node in the binary tree. So root will always be 0 
    # The height represents the longest distance between node to leaf 
    # In the max depth problem on leetcode we actually need to find the height of the tree from root to leaf node 
    def determineHeight(self, root): 
        # Base case, since this is a recursive function
        if not root: 
            return 0 
        
        # Find the deepest to the left 
        left = self.determineHeight(root.left)
        # Find the deepest to the right
        right = self.determineHeight(root.right)
        
        height = max(left, right) + 1
        
        return height 
        
    # The diameter of a tree represents the longest distance from a leaf to whatever node. longest distance between two nodes
    def findDiameter(self, root):
        maxDiameter = 0 
        # This returns the height and calculates diameter
        def calculateHeight():
            # Base case 
            if not root:
                return 0
            
            # To calculate it we need to calculate the height on the left side and the height on the right side 
            left = self.determineHeight(root.left)
            right = self.determineHeight(root.right)

            
            # We can use a global variable -> or nonlocal variable
            nonlocal maxDiameter
            # The diameter is the sum of the left height + right height. We need to find the max diameter so we do a max(diam, left+right)
            maxDiameter = max(maxDiameter, left + right) 
            
        
            return max(left, right) + 1
        calculateHeight()
        return maxDiameter
    
    # Definitions -> 
    # Balanced binary tree  = A binary tree is balanced when the difference between left and right doesn't exceed 1 
    # So if the height of left is 4 and the height of right is 6, it's not balanced. 
    # In order to do this: 
    # We calculate the height of both 
    # We add them, if at some point it's > 1 we return False, else we return true 
    def determineBalancedTree(self, root):
        difference = 0
        def calculateHeight(root):
            # Base case, we return 0 when there's no root - when we are at a leaf node
            if not root: 
                return 0 
            
            left = calculateHeight(root.left)
            right = calculateHeight(root.right)
            nonlocal difference
            difference = max(difference, abs(right - left))
              
            return max(left, right) + 1 
        calculateHeight(root)
        return False if difference > 1 else True
    
    
# Two trees are the same when the have the same data AND the same structure 
# We need to do traversal through both of them and return false if a value is not the same 
def determineSameTree(tree1, tree2):
    # Base case -> if both are missing then they are the same
    if not tree1 and not tree2: 
        return True
    
    # If tree1 is missing but tree2 is not -> they are not the same
    # If tree1's data is different to tree2's data -> they are not the same 
    if not tree1 or not tree2 or tree1.data != tree2.data: 
        return False 
    
    # We do this with tree 1 and tree 2 on the left and on the right
    leftSide = determineSameTree(tree1.left, tree2.left)
    rightSide = determineSameTree(tree1.right, tree2.right) 
    
    return leftSide and rightSide

# A sub tree is a node inside a root node that's identical in both structure and data. 
def determineIfSubtree(tree1, tree2):
    
    # An empty tree is considered a subtree of any other tree **
    if not tree2:
        return True
    
    if not tree1:
        return False
    
    if determineSameTree(tree1, tree2):
        return True
    # Idea -> preorder traversal through tree1
    # Call the determineSameTree function over each node in the traversal 
    # If it return true we found the answer 
    leftSide = determineIfSubtree(tree1.left, tree2)
    rightSide = determineIfSubtree(tree1.right, tree2)
    # If tree2 is a subtree at either side, it means we found the response 
    return leftSide or rightSide

    
    
        
    
# Rules of tree are mid is higher than left but not higher than right 
tree = TreeNode(10)
tree.left = TreeNode(4)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(5)
tree.right = TreeNode(12)
tree.right.left = TreeNode(11)
tree.right.right = TreeNode(13)
print(tree.determineHeight(tree))
# revTree = tree.reverseBinaryTree(tree)
# print(revTree.inOrderTraverse(revTree))