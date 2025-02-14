# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        while p1.next != None or p2.next != None:
            if p1.next == None and p2.next != None:
                p1.next = ListNode(0)
            elif p1.next != None and p2.next == None:
                p2.next = ListNode(0)
            p1 = p1.next
            p2 = p2.next
        p1 = l1
        p2 = l2
        l3 = ListNode(0)
        p3 = l3
        sum = 0
        while p1:
            tmp_value = p1.val + p2.val + sum
            sum = int(tmp_value / 10)
            s = tmp_value % 10
            p3.next = ListNode(s)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        if sum == 1:
            p3.next = ListNode(1)
        return l3.next



# leetcode submit region end(Prohibit modification and deletion)
