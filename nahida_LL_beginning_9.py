class Node:
   def __init__(self, data = None, next = None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = Node()

   def display(self):
      if self.head is None:
         print('empty')
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

if __name__ == '__main__':
   AB = LinkedList()
   AB.append_at_begining(8)
   AB.append_at_begining(7)
   AB.append_at_begining(6)
   AB.append_at_begining(5)
   AB.append_at_begining(4)
   AB.append_at_begining(3)
   AB.display()



