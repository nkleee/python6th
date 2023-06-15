#연결리스트의 노드를 표현할 클래스 정의
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

#스택을 표현할 클래스 정의
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    #스택이 비어있는지 확인하는 메서드
    def is_empty(self):
        return self.size == 0

    #스택의 맨 위에 원소를 추가하는 메서드
    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    #스택의 맨 위에서 원소를 꺼내는 메서드
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

stack = Stack()

#스택에 원소추가
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(5)


for _ in range(5):
    print(stack.pop()) #스택에서 원소 꺼냄