from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
    
    def insertNode(self, newNodeData):
        if self.val is None: 
            self.val = newNodeData
            
        if newNodeData < self.val: 
            if self.left is None: 
                self.left = TreeNode(newNodeData)
            else: 
                self.left.insertNode(newNodeData)
        else:
            if self.right is None:
                self.right = TreeNode(newNodeData)
            else:
                self.right.insertNode(newNodeData)

    def inOrderTraversal(self, root):
        res = []
        if root: 
            res = self.inOrderTraversal(root.left)
            res.append(root.val)
            res = res + self.inOrderTraversal(root.right)
        return res 
    def findDepth(self, root):
        if root is None: 
            return 0
        
        lHeight = self.findDepth(root.left)
        rHeight = self.findDepth(root.right)
        
        return max(lHeight, rHeight) + 1

    def findDepthItrs(self, root):
        if root is None: 
            return 0 
        
        # Root node
        queue = deque([root])
        depth = 0
        
        while queue:
            # Calculates the size at the level depending on the queue len
            level_size = len(queue)
            for _ in range(level_size):
                # Dequeues the node
                node = queue.popleft()
                # Enqueues the elements from left and right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(depth)
            depth += 1
        return depth 

tree = TreeNode(3)

tree.left = TreeNode(9)

tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

tree.findDepthItrs(tree)
# Objective = Return max depth of binary search tree (Farthest leaf node)
# Left - right - root 
# Post-Order traversal





