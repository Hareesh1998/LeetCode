class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and not carry:
            return None

        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        result = ListNode(sum % 10)
        result.next = self.addTwoNumbers(l1, l2, sum // 10)
        return result
