class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Heap:
    def __init__(self):
        self.root = None

    #insertNode function that checks where to add the node
    def insertNodeToTheTree(self,newNode:int)->None:
        #case 1: there is no root node
        if not self.root:
            self.root = TreeNode(newNode)
        #case 2: root exists and now recursion needs to take place to see where to add node
        
        def dfs(node):
            
            if not node.right and not node.left:
                node.left = TreeNode(newNode)
            dfs(node.left)

                
        

heap = Heap()
heap.insertNode(3)
heap.insertNode(4)
heap.insertNode(5)


        



