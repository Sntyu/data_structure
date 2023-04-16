class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

def create_linklist_head(lk):
    head=Node(None)
    for element in lk:
        node=Node(element)
        node.next=head.next
        head.next=node
    return head.next


def create_linklist_tail(lk):
    head=Node(None)
    tail=head
    for element in lk:
        node=Node(element)
        tail.next=node      #把尾部指针指向新节点
        tail=node           #把尾部修改为新节点
    return head.next

def print_linklist(lk):
    while lk:
        print(lk.item,end=  ',')
        lk=lk.next

lk=create_linklist_head([1,2,3])
print_linklist(lk)


