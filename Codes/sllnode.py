# Create a node in Singly linked list 

class Node :
    def __init__(self,data= None,next= None):
        self.data = data
        self.next = next

# Create a node 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# print data by traversing 
curr_node = node1

while curr_node is not None :
    print("Current node is :",curr_node.data)
    curr_node = curr_node.next
