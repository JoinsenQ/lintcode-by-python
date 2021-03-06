"""
描述
在 O(n log n) 时间复杂度和常数级的空间复杂度下给链表排序。

 
样例
给出 1->3->2->null，给它排序变成 1->2->3->null.

挑战
分别用归并排序和快速排序做一遍。
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    # 归并法
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        pre = head
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        left = head  
        right = pre.next  
        pre.next = None  
        left = self.sortList(left)  
        right = self.sortList(right)  
        return self.merge(left,right)
        
    def merge(self, left, right):
        pre = ListNode(-1)
        first = pre
        while left and right:
            if left.val < right.val:
                pre.next = left
                pre = left
                left = left.next
            else:
                pre.next = right
                pre = right
                right = right.next
        if left:
            pre.next = left
        else:
            pre.next = right
                
        return first.next
    
    
