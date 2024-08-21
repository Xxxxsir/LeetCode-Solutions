# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:
        head = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                num1 =l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            
            sum = num1+num2+carry
            if sum >= 10:
                sum = sum%10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(sum)
            curr = curr.next

        return head.next
            
        