# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2

        num1 = 0
        num2 = 0

        i = 0
        j = 0
        while curr1:
            num1 += curr1.val * 10 ** i
            curr1 = curr1.next
            i += 1

        while curr2:
            num2 += curr2.val * 10 ** j
            curr2 = curr2.next
            j += 1

        sum = num1 + num2

        # ListNode 생성 함수
        def int_to_listnode(num):
            # 첫 자릿수 노드 생성
            head = ListNode(num % 10)
            num //= 10
            current = head

            # 나머지 자릿수 반복 처리
            while num > 0:
                current.next = ListNode(num % 10)
                num //= 10
                current = current.next

            return head

        result = int_to_listnode(sum)
        return result
        