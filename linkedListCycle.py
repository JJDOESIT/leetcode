class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    l = []
    while head is not None:
        if head in l:
            return True

        l.append(head)
        head = head.next

    return False


head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n1

print(hasCycle(head))
