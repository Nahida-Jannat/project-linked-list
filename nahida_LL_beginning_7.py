#linked list implementation

class Node:
   def __init__(self, data = None, next =None):
      self.data = data
      self.next = next

class Linkedlist:
   def __init__(self):
      self.head =Node()
   
   def display(self):
      if self.head is None:
         print("empty")
         return
      current_node = self.head
      info_str = ''
      while current_node:
         info_str = info_str + str(current_node.data) + '-->'
         current_node =current_node.next
      print(info_str)

   def add_at_beginning(self, data):
      node = Node(data, self.head.next)
      self.head.next = node

a = Linkedlist()

a.add_at_beginning(123)
a.add_at_beginning(456)
a.add_at_beginning(789)
a.display()
