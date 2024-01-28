class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print("\n")

def reverse_ll(node):
    if node.next is None:
        global head
        head = node
        return node
    temp = reverse_ll(node.next)
    node.next = None
    temp.next = node
    return node


array = [5,3,2,1]
head, prev = None, None

for i in array:
    node = Node(i)

    if head is None:
        head = node
        prev = head
    else:
        prev.next = node
        prev = node

print_ll(head)
reverse_ll(head)

"""
visitors = [head]
resp = []
i = 0
while visitors:
    root = visitors[i]
    if root.left:
        visitors.append(root.left)
        i+=1
        continue
    elif root.right:
        visitors.append(root.right)
        i+=1
        continue
    else:
        del visitors[i]
        resp.append(root.val)
        


visitors = [1,2,]
resp = [5,]
"""






    


