class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insertNode(self,root:TreeNode, elemToInsert:int)->TreeNode:
        if not root:
            return TreeNode(elemToInsert)
        
        if elemToInsert < root.val:
            root.left = self.insertNode(root.left,elemToInsert)
        else:
            root.right = self.insertNode(root.right,elemToInsert)
        return root
    
    def preOrder(self,root:TreeNode)->list:
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res 

       
        
tree = Tree()
tree.insertNode(2)
tree.insertNode(3)
tree.insertNode(5)
print(tree.preOrder(tree.root))


