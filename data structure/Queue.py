class Queue:
    def __init__(self,size=100):
        self.queue=[0 for _ in range(size)]
        self.size=size
        self.rear=0
        self.front=0

    def push(self,element):
        if not self.is_filled():
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            raise IndexError("Queue is full")

    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError("queue is_empty")

    def is_empty(self):
        return self.rear==self.front

    def is_filled(self):
        return (self.rear+1)%self.size==self.front

from collections  import deque
# queue=deque([1,2,3])
# queue.append(1)
# queue.popleft()
#
# queue.appendleft(1)
# queue.pop()
def tail(n):
    f=open("txt_1",'r')
    # q=deque(f,n)
    print (f.readlines())
    # return q

tail(3)




