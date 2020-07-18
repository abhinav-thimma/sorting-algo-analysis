class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + ' ' + str(self.val) + ' ' + str(self.right) 

class BST:
    root: TreeNode = None

    def insertNode(self, val:int, comparator):
        node = TreeNode(val, None, None)
        # first node
        if(self.root == None):
            self.root = node
            return
        
        pointer, parent = self.root, self.root
        while(pointer!= None and (pointer.left != None or pointer.right != None)):
            parent = pointer
            pointer = pointer.left if(comparator(val, pointer.val)) else pointer.right

        pointer = pointer if(pointer != None) else parent
        
        if(comparator(val, pointer.val)):
            pointer.left = node
        else:
            pointer.right = node
        return

    def get_sorted_arr(self):
        sortedArr = []
        self.inorder_insertion(self.root, sortedArr)
        return sortedArr

    def inorder_insertion(self, root, sortedArr):
        if(root != None):
            self.inorder_insertion(root.left, sortedArr)
            sortedArr.append(root.val)
            self.inorder_insertion(root.right, sortedArr)
    
    def __str__(self):
        return str(self.root)

class Sort:
    def tree_sort(self, nums, order = 'asc'):
        if(nums == None or len(nums) < 1):
            return nums, 0
        comparator = lambda x, y: (x < y)  if (order == 'asc') else (x > y)
        bst, array_access_count = BST(), 0
        for num in nums:
            bst.insertNode(num, comparator)
            array_access_count += 1
        # inorder traversal takes n array accesses
        array_access_count += len(nums)
        return bst.get_sorted_arr(), array_access_count
