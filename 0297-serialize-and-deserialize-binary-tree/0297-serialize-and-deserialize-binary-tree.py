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
        if not root:
            return ""
        q = []
        s = []
        q.append(root)
        while q:
            node = q.pop(0)
            if not node:
                s.append("#")
            else:
                s.append(str(node.val))
            if node:
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        index = 0
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = []
        q.append(root)
        while q:
            node = q.pop(0)

            index += 1
            if data[index] == "#":
                node.left = None
            else:
                newnode = TreeNode(int(data[index]))
                node.left = newnode
                q.append(newnode)
            
            index += 1
            if data[index] == "#":
                node.right = None
            else:
                newnode = TreeNode(int(data[index]))
                node.right = newnode
                q.append(newnode)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))