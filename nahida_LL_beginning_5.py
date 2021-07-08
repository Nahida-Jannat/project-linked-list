#linked list implementation
#Add values at begenning in linked list
#Node --> Data | Next

class Node:
   def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = Node()
      
   def display(self):
      if self.head is None:
         print("Linked list is empty")
         return
      current_node = self.head
      info_str =''
      while current_node:
         info_str = info_str + str(current_node.data) + '-->'
         current_node = current_node.next
      print(info_str)

   def append_at_beginning(self, data):
      node = Node(data, self.head.next)
      self.head.next = node
      
if __name__ == '__main__':
   ll = LinkedList()

   #item added at beginning
   ll.append_at_beginning(1)
   ll.append_at_beginning(2)
   ll.append_at_beginning(3)
   ll.append_at_beginning(4)
   ll.append_at_beginning(5)
   ll.append_at_beginning(6)
   ll.append_at_beginning(7)
   ll.append_at_beginning(8)

   ll.display()
