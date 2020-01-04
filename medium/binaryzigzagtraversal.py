# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # we'll need some BFS type of search, and then at each level
        # we determine whether it's odd or even, then we can figure out how we want to print
        # how do we do BFS again in tree?
        # i feel like we need a list of nodes at the current level, before deciding how to print
        currLevel = []
        tmp = []
        temp = []
        result = []
        currLevel.append(root)
        level = 1
        if root == None:
            return None

        while True:
            if currLevel == []:
                return result
            # print(currLevel)
            if level % 2 == 1:
                for node in currLevel:
                    temp.append(node.val)
                    if node.left != None:
                        tmp.append(node.left)
                    if node.right != None:
                        tmp.append(node.right)
            else:
                for node in reversed(currLevel):
                    temp.append(node.val)
                    if node.right != None:
                        tmp.insert(0, node.right)
                    if node.left != None:
                        tmp.insert(0, node.left)
            result.append(temp)
            currLevel = tmp
            tmp = []
            temp = []
            level += 1

# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
