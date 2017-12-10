class Solution(object):
    def ave(self, node, level):
        if self.all_pos.has_key(level):
            self.all_pos[level][0] += node.val
            self.all_pos[level][1] += 1
        else:
            self.all_pos[level] = [node.val, 1]
        if node.left:
            self.ave(node.left, level+1)
        if node.right:
            self.ave(node.right, level+1)
            
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.all_pos = {}
        self.ave(root, 1)
        result = []
        level = 1
        while self.all_pos.has_key(level):
            result.append(self.all_pos[level][0] * 1.0 / self.all_pos[level][1])
            level += 1
        return result
        
