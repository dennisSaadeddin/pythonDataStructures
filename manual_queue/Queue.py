from manual_queue.QueueElem import MyQueueElement


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.is_empty = True

    def enqueue(self, elem):
        tmp = MyQueueElement(elem)
        if self.head is None:
            self.head = tmp
        if self.tail is not None:
            self.tail.next = tmp
        self.tail = tmp
        self.is_empty = False

    def dequeue(self):
        if self.is_empty:
            print("Queue is empty.")
        else:
            self.head = self.head.next

        if self.head is None:
            self.is_empty = True

    def front(self):
        if self.is_empty:
            print("Queue is empty. There's no front element.")
        else:
            print("Head: ", self.head.data)

    def rear(self):
        if self.is_empty:
            print("Queue is empty. There's no rear element.")
        else:
            print("Tail: ", self.tail.data)

    def print_queue(self):
        tmp = self.head
        while tmp is not None:
            if tmp.next is None:
                print(tmp.data)
            else:
                print(tmp.data, " - ", end="", flush=True)
            tmp = tmp.next


breadQueue = MyQueue()
breadQueue.enqueue(1)
breadQueue.enqueue(2)
breadQueue.enqueue(3)
breadQueue.enqueue(4)
breadQueue.enqueue(5)
breadQueue.enqueue(6)
breadQueue.enqueue(7)

breadQueue.front()
breadQueue.rear()

if breadQueue.is_empty:
    print("The queue is empty. Please add elements.")
else:
    print("Here's your queue: ")
    breadQueue.print_queue()

breadQueue.dequeue()
breadQueue.print_queue()
breadQueue.dequeue()
breadQueue.print_queue()
breadQueue.dequeue()
breadQueue.print_queue()
breadQueue.dequeue()
breadQueue.print_queue()
breadQueue.dequeue()
breadQueue.print_queue()
breadQueue.dequeue()
breadQueue.print_queue()
breadQueue.dequeue()
breadQueue.print_queue()

breadQueue.front()
breadQueue.rear()

if breadQueue.is_empty:
    print("The queue is empty. Please add elements.")
else:
    print("Here's your queue: ", breadQueue.print_queue())


if __name__ == "__main__":
    MyQueue()



