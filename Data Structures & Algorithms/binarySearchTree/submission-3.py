class TreeNode:
    def __init__(self,key: int, val: int, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            new_node = TreeNode(key, val)
            self.root = new_node
            return
        existing = self.searchBST(self.root, key)
        if existing:
            existing.val = val
        else:
            self.insertIntoBST(self.root, key, val)
        
    def insertIntoBST(self, root_node: Optional[TreeNode], key: int, val: int):
        if not root_node:
            return TreeNode(key,val)
            
        if key < root_node.key:
            root_node.left = self.insertIntoBST(root_node.left, key, val)
        elif key > root_node.key:
            root_node.right = self.insertIntoBST(root_node.right,key, val)
        return root_node
        
        

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        node = self.searchBST(self.root, key)
        if node:
            return node.val
        else:
            return -1

    def searchBST(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
            
        if key < root.key:
            return self.searchBST(root.left, key)
        elif key > root.key:
            return self.searchBST(root.right,key)
        else:
            return root

    def getMin(self) -> int:
        if not self.root:
            return -1
        elif not self.root.left:
            return self.root.val
        else:
            curr = self.root
            while curr.left:
                curr = curr.left
            return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        elif not self.root.right:
            return self.root.val
        else:
            curr = self.root
            while curr.right:
                curr = curr.right
            return curr.val


    def remove(self, key: int) -> None:
        def minNode(root: Optional[TreeNode]) -> Optional[TreeNode]:
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr 

        def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
                return None
        
            if key < root.key:
                root.left = deleteNode(root.left, key)
            elif key > root.key:
                root.right = deleteNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min = minNode(root.right)
                    root.key = min.key
                    root.right = deleteNode(root.right, min.key)
            return root
        self.root = deleteNode(self.root, key)


    def getInorderKeys(self) -> List[int]:
        res_array = []
        def inOrder(root: Optional[TreeNode]):
            if not root:
                return
            inOrder(root.left)
            res_array.append(root.key)
            inOrder(root.right)
        inOrder(self.root)
        return res_array

    def getPreorderKeys(self) -> List[int]:
        res_array = []
        def preOrder(root: Optional[TreeNode]):
            if not root:
                return
            res_array.append(root.key)
            inOrder(root.left)
            inOrder(root.right)
        inOrder(self.root)
        return res_array