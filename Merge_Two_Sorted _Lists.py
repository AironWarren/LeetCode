# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


s = [1, 2, 3]
s2 = [1, 3, 4]

sam = (s + s2)
sam.sort()

print(sam)

# print(Solution.mergeTwoLists(s, s2))
