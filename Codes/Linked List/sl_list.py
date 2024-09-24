class Node:
    def __init__(self,item = None, next = None):
        self.item = item 
        self.next = next

class SLL:
    def __init__(self,start = None):
        self.start = start      # points head
    def is_empty(self):
        return self.start ==None   #check if empty
    
    def insert_at_first(self,data):
        n = Node(data, self.start)
        self.start = n
    
    def insert_at_last(self,data):
        n = Node(data)
        
            
        