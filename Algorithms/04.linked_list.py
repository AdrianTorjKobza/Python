class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Node data: %s" % self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        
        while current:
            count = count + 1
            current = current.next_node
    
        return count
    
    # Add a new node at the head of the list.
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # Search target in the linked list.
    def search(self, target):
        current = self.head

        while current:
            if current.data == target:
                return current
            else:
                current = current.next_node
        
        return None

    def __repr__(self):
        nodes = []
        current = self.head # Set 'current' to the head node.

        while current:
            # Check if 'current' is the head node.
            if current is self.head: 
                nodes.append("[Head: %s]" % current.data)
            # Check if we are the tail node.
            elif current.next_node is None: 
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node #Move forward in the linked list.
        
        return ' -> '.join(nodes) # Join all the strings inside the nodes list.

l = LinkedList()

for i in range (11):
    l.add(i)

print(l)
# [Head: 10] -> [9] -> [8] -> [7] -> [6] -> [5] -> [4] -> [3] -> [2] -> [1] -> [Tail: 0]

result = l.search(7)
print(result)
# Node data: 7