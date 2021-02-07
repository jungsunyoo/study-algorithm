

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# testing
node = Node(3)
first_node = Node(4)
node.next = first_node
# print(node.next.data)
# print(node.data)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next # 한칸한칸 다음으로 이동
        cur.next = Node(data)
        print(cur.data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)


linked_list.print_all()