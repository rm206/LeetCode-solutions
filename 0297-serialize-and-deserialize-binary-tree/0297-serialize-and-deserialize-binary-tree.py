# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        res = []
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node
        
        vals = data.split(",")
        self.i = 0
        res = helper()
        return res
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))