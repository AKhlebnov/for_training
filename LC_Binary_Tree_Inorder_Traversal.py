"""
94. Binary Tree Inorder Traversal.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # Движемся влево, добавляя узлы в стек
            while current:
                stack.append(current)
                current = current.left
            # Посещаем узел
            current = stack.pop()
            result.append(current.val)
            # Переходим к правому поддереву
            current = current.right

        return result


root = TreeNode(
    1,  # Корень дерева
    TreeNode(
        2,  # Левый ребёнок корня
        TreeNode(4),  # Левый ребёнок узла 2
        TreeNode(
            5,  # Правый ребёнок узла 2
            TreeNode(6),  # Левый ребёнок узла 5
            TreeNode(7)   # Правый ребёнок узла 5
        )
    ),
    TreeNode(
        3,  # Правый ребёнок корня
        None,  # Левый ребёнок узла 3 (отсутствует)
        TreeNode(8, TreeNode(9))  # Правый ребёнок узла 3 с дочерним узлом 9
    )
)

sol = Solution()

print(sol.inorderTraversal(root))

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?