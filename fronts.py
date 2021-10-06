class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None


#  NOT WORKING -> RETURN VALUE OT HEAD OF LISTls 
    def front(self, index):
        current = self.head
        count = 0
        if (count == index):
            return current.data
        return self

    def addFront(self, val):
        new_node = Node(val)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node
        return self

    def printVals(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
        return self

    def removeFront(self):
        if self.head != None:
            self.head = self.head.next
        return self

sll=SLL()
sll.addFront(5)
sll.addFront(10)
sll.addFront(15)
sll.removeFront()
sll.printVals()

sll.front(0)