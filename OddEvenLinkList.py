class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def listtoListNode(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def oddEvenList(Numbers):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    head = listtoListNode(Numbers)
    tempList = []
    even = x = ListNode(0)
    odd = y = ListNode(0)
    while (head):
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None
    odd.next = y.next
    return x.next
m = oddEvenList([1,2,3,4,5])
while(m):
    print(m.val)
    m = m.next
