class Solution(object):
    def _pathSum(self, node, remain):
            self.stack.append(node.val)
            if (not node.left) and (not node.right):
                if remain == node.val:
                    self.totalList.append(copy.deepcopy(self.stack))
            else:
                next_remain = remain - node.val
                if node.left:
                    self._pathSum(node.left, next_remain)
                if node.right:
                    self._pathSum(node.right, next_remain)
            self.stack.pop()
            
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.totalList = []
        self.stack = []
        remain = sum
                
        if root:
            self._pathSum(root, remain)
        return self.totalList
