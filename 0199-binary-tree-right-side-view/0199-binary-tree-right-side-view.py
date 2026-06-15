from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #in level order traversal, the right most children are what you will see

        if root is None:
            return []
        
        q = deque([root])
        visited = []

        while q:
            s = len(q)
            level = []

            for i in range(s):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)
            
            if level != []:
                visited.append(level[-1])
        
        return visited 