'''
In the below code add try catces too 
as well as cover all false condition like negative index, index more than length
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        curr = self.head
        self.head = new_node
        self.head.next = curr
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)
        print("total length:", self.length)

    def deleteNode(self, data):
        curr = self.head
        if self.head is None:
            self.tail = None
            return
        # if data is head
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        
        # current is either next item of head till tail
        while curr:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.length -= 1
                return
            curr = curr.next

    def replaceNode(self, index, data):
        print(index)
        cnt = 0
        curr = self.head
        
        while curr:
            if cnt == index:
                curr.data = data
                return
            cnt += 1
            curr = curr.next
    
    def insertNodeAtIndex(self, index, data):
        # assign head to current
        new_node = Node(data)
        curr = self.head
        cnt = 0
        while curr:
            # if index is 0 : need to insert before head
            if index ==  0:
                self.head = new_node
                self.head.next = curr
                self.length += 1
                return
            if cnt == (index - 1):
                temp = curr.next
                curr.next = new_node
                curr = curr.next
                curr.next = temp
                self.length += 1
                return
            cnt += 1
            curr = curr.next
    def removeNodeAtIndex(self, index):
        # if head is None
        cnt = 0
        curr = self.head
        if self.head is None:
            self.tail = None
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        while curr:
            if cnt == (index - 1):
                curr.next = curr.next.next
                self.length -= 1
                return
            curr = curr.next
            cnt += 1
    
    def reverseLinkedList(self):
        curr = self.head
        prev = None
        if self.head is None:
            raise ValueError("List is empty")
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
   
            
ll = LinkedList()
ll.prepend(5)
ll.prepend(24)
ll.append(10)
ll.append(20)
ll.append(45)
ll.append(90)
ll.prepend(110)
ll.traverse()
ll.deleteNode(90)
ll.traverse()
ll.replaceNode(5, 200)
ll.traverse()
ll.insertNodeAtIndex(6, 250)
ll.traverse()
ll.removeNodeAtIndex(2)
ll.traverse()
ll.reverseLinkedList()
ll.traverse()
