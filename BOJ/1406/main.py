import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)  # Dummy head
        self.tail = Node(None)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail  

    def append(self, data):
        new_node = Node(data)
        prev_node = self.tail.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.cursor = self.tail

    def insert(self, data):
        new_node = Node(data)
        prev_node = self.cursor.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.cursor
        self.cursor.prev = new_node

    def delete(self):
        if self.cursor.prev != self.head:
            to_delete = self.cursor.prev
            prev_node = to_delete.prev
            next_node = self.cursor
            prev_node.next = next_node
            next_node.prev = prev_node

    def move_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def to_string(self):
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.data)
            current = current.next
        return ''.join(result)

# 입력 처리
input = sys.stdin.readline

dll = DoubleLinkedList()
initial_string = input().rstrip()

for char in initial_string:
    dll.append(char)

tc = int(input())

for _ in range(tc):
    command = input().rstrip()
    
    if command[0] == 'P':
        data = command.split(' ')[1]
        dll.insert(data)
    elif command == 'L':
        dll.move_left()
    elif command == 'D':
        dll.move_right()
    elif command == 'B':
        dll.delete()

print(dll.to_string())