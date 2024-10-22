# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Указатель на начало результирующего списка
        current = dummy_head  # Указатель на текущий узел результата
        carry = 0  # Переменная для переноса

        while l1 or l2 or carry:
            # Получаем значения текущих узлов или 0, если узел отсутствует
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Считаем сумму и перенос
            total = val1 + val2 + carry
            carry = total // 10  # Обновляем перенос
            # Создаем новый узел с последней цифрой суммы
            current.next = ListNode(total % 10)
            current = current.next  # Переходим к следующему узлу

            # Переход к следующему узлу в списках, если они не закончились
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Возвращаем результат, начиная с первого узла
