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
    
    #root,left,right
    def preOrder(self,root:TreeNode)->list:
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    
    #left,root,right
    def inOrder(self,root:TreeNode)->list:
        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    
    #left,right,root
    def postOrder(self,root:TreeNode)->list:
        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
        




       
        
tree = Tree()
tree.root = tree.insertNode(tree.root,2)
tree.root = tree.insertNode(tree.root,1)
tree.root = tree.insertNode(tree.root,5)
tree.root = tree.insertNode(tree.root,0)
print(tree.preOrder(tree.root))
print(tree.inOrder(tree.root))
print(tree.postOrder(tree.root))



