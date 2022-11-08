from ctypes import sizeof


class Node:
    def __init__(self,k):
        self.next=None
        self.key=k
        

def printList(head,x):
    pos=1
    curr=head
    while curr!=None:
        if curr.key==x:
            return pos

        pos=pos+1

        curr=curr.next

    return -1


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print(printList(head,10))


