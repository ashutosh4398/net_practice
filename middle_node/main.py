# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # find the length of the linked list
    ll_length: int = 0
    head: LinkedList = linkedList
    while (head != None):
        ll_length += 1
        head = head.next
    # 1 2 3 4 5
    # find middle, leveraging 0 based indexing
    mid_elem: int = ll_length // 2
    currentNode: LinkedList = linkedList
    for _ in range(mid_elem):
        currentNode = currentNode.next
    

    return currentNode.value


ll = LinkedList(10)
print(middleNode(ll))