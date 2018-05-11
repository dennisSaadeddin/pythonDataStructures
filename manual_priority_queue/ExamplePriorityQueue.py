from queue import PriorityQueue


class MyPriorityQueue(object):
    q = PriorityQueue()

    q.put(('a', 'Dan'))
    q.put(('b', 'Karen'))
    q.put(('c', 'Louis'))
    q.put(('c', 'Nikola'))
    q.put(('x', 'Alex'))
    q.put(('z', 'Bob'))
    q.put(('w', 'Alice'))

    while not q.empty():
        print(q.get())

    print()
    if q.empty():
        print("The priority Queue is empty")


if __name__ == "__main__":
    MyPriorityQueue()