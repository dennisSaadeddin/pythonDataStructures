from Node import NodeElement


class myLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = NodeElement(data)  # start from the first node

        if self.head is None:
            self.head = node
        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node

    def delete(self, p):
        if p is self.head:
            self.head = p.next
            p.next = p.prev
        elif p is self.tail:
            self.tail = p.prev
            p.prev.next = p.next
        else:
            tmp = p.prev
            tmp.next = p.next
            p.next.prev = tmp

    def search(self, val):
        temp = self.head
        if temp is not None:
            while temp.next is not None:
                if temp.data is val:
                    return temp
                temp = temp.next
            if temp.data is val:
                return temp
        else:
            return None

    def print_value(self):
        temp = self.head
        while temp is not None:
            if temp.next is not None:
                print(temp.data, "-> ", end="", flush=True)
            else:
                print(temp.data)
            temp = temp.next


myList = myLinkedList()

myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)
myList.add(6)
myList.add(7)

myList.print_value()

if myList.search(1) is not None:
    print("I've got your value in my list!")
else:
    print("I haven't found the value in my list.")

myList.delete(myList.search(7))
myList.print_value()

myList.delete(myList.search(1))
myList.print_value()

myList.delete(myList.search(4))
myList.print_value()

if __name__ == "__main__":
    myLinkedList()
