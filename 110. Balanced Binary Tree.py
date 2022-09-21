"""110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:
Input: root = []
Output: true
 Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balancecheck(root):
            ## if no child nodes are present return height 0 and balanced true
            if not root: return [True,0]
            ## Recursive call to left and right function
            left,right=balancecheck(root.left),balancecheck(root.right)
            ## To calculate balance left[0]-- checks if till now balanced and abs part will check if height difference till now is under or 1 
            balanced = (left[0] and right[0] and abs(left[1]-right[1])<=1)
            ## returning if balanced and calculating height of nth nodes ( bottoms up approach is here )
            return [balanced, 1 + max(left[1],right[1])]
        return balancecheck(root)[0]