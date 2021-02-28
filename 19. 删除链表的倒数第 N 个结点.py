"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0, head)
        fast = head
        slow = res

        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return res.next