#linked list implementation
#add value at bwginning

class Node:
   def __init__(self, data=None, next= None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = Node()

   def display(self):
      if self.head is None:
         print('Empty')
         return
      current_node = self.head
      info_str = ''
      while current_node:
         info_str = info_str + str(current_node.data) + '-->'
         current_node = current_node.next
      print(info_str)

   def append_at_begining(self, data):
      node = Node(data, self.head.next)
      self.head.next = node

#item added at begining

B = LinkedList()
B.append_at_begining(5)
B.append_at_begining(4)
B.append_at_begining(3)
B.append_at_begining(2)
B.append_at_begining(1)
B.display()