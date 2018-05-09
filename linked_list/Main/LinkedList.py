from Main import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data)  # start from the first node

        if self.head is None:
            self.head = node
        if self.tail is not None:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node

    def delete(self, node):
        temp = node.prev
        node.prev.next = node.next
        node.next = temp

    def search(self, val):
        temp = self.head
        if temp is not None:
            while temp.next is not None:
                if temp.data is val:
                    return True
                else:
                    return False
                temp = temp.next
            if temp.data is val:
                return True
            else:
                return False
        else:
            return False

    def print_value(self):
        temp = self.head
        while temp is not None:
            if temp.next is not None:
                print(temp.data, "-> ", end="", flush=True)
            else:
                print(temp.data)
            temp = temp.next


myList = LinkedList()

myList.add(1)
myList.add(2)
myList.add(3)

myList.print_value()

if myList.search(4) is True:
    print("We got your value in our list!")
else:
    print("We haven't found the value in our list.")


if __name__ == "__main__":
    LinkedList()
