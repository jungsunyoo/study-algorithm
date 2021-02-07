class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 어떻게 하면 될까요?
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

        # Node(value).next = self.head
        # self.head = Node(value) -> 이게 안된 이유는 Node를 한번 더 호출해서?!


    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is Empty"
        else:
            newhead = self.head
            self.head = self.head.next
            return newhead

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None
        # 어떻게 하면 될까요?
        # if self.head.next == None:
        #     return True
        # else:
        #     return False

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop().data)
print(stack.is_empty())