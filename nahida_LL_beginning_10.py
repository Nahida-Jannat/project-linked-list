class Node:
   def __init__(self, data = None, next = None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = Node()

   def display(self):
      if self.head is None:
         print("Empty")
         return
      current_node = self.head
      info_str = ''
      while current_node :
         info_str = info_str + str(current_node.data) + '-->'
         current_node = current_node.next
      print(info_str)

   def append_at_begining(self,data):
      node = Node(data, self.head.next)
      self.head.next = node

LL = LinkedList()
LL.append_at_begining(555)
LL.append_at_begining(444)
LL.append_at_begining(333)
LL.append_at_begining(222)
LL.display()