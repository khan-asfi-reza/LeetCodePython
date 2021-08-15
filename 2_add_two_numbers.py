"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1: ListNode, l2: ListNode) -> ListNode:
    # Create A Node
    summationNode = ListNode()
    # Set Current Pointer, pointing to the working Node
    current = summationNode
    # Carry
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        # Get Total Result
        current_val_total = l1_val + l2_val + carry
        # Get the carry number
        carry = current_val_total // 10
        # Get the remainder
        current_val = current_val_total % 10

        # Assignment of Current Pointer
        current.next = ListNode(current_val)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return summationNode.next
