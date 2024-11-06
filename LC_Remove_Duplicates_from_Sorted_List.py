"""
83. Remove Duplicates from Sorted List.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp_node = head

        while temp_node and temp_node.next:

            if temp_node.val == temp_node.next.val:
                temp_node.next = temp_node.next.next

            else:
                temp_node = temp_node.next

        return head


head_3 = ListNode(2)
head_2 = ListNode(1, head_3)
head_1 = ListNode(1, head_2)

sol = Solution()
result = sol.deleteDuplicates(head_1)

while result:
    print(result.val)
    result = result.next


# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
