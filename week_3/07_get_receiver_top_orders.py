top_heights = [6, 9, 5, 7, 4]


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


def get_receiver_top_orders(heights):
    highest_ind = 0
    # received=[]
    # received = Stack()
    received = [0,0,0,0,0]
    for i in range(0, len(heights) - 1):
        curr_ind = len(heights) - i - 1
        for j in range(0, curr_ind - 1):
            if heights[curr_ind - 1 - j] > heights[curr_ind]:
                received[len(heights)-1-i] = curr_ind - j
                break
            # received.push(0)
    return received


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
