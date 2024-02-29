'''
todo
1. insert node at beginning - done
2. insert node at end - done
3. traverse - done
4. search a number
5. insert node after certain index or number 
6. delete node of certain index
7. find minimum number and delete
8. find maximum number and delete
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    # insert at beginning, prepend
    def insert_at_beginning(self, data):
        # create a new node
        print("---------Insert node at beginning ---------")
        new_node = Node(data)
        new_node.next = self.head
        self.head =  new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1

    # this can be written as append
    def insert_at_end(self, data):
        print("---------Insert node at end ---------")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None)

    def delete(self, data):
        # 1. head is None
        if self.head is None:
            self.tail = None
            return
        
        # 2. if data is head
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        # curr is either next item of head till the tail
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data:
                prev.next = curr.next
                if curr.data == self.tail:
                    self.tail = prev
                self.length -= 1
                return
            # if not matched, move prev pointer to curr and curr to next
            prev = curr
            curr = curr.next
            
            
                

linkedList = LinkedList()
linkedList.insert_at_beginning(5)
# linkedList.insert_at_end(10)
# linkedList.insert_at_end(40)
# linkedList.insert_at_end(50)
# linkedList.insert_at_end(96)
linkedList.traverse()
linkedList.delete(5)
linkedList.traverse()
