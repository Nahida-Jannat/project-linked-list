# Linked list implementation
# Add value at end in linked list

# NODE --> Data | Next
class Node:
   def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = Node()

   def print_linked_list(self):
      if self.head is None:
         print('Linked list is empty')
         return
      current_node = self.head
      info_str = ''
      while current_node:
         info_str = info_str + str(current_node.data) + ' --> '
         current_node = current_node.next
      print(info_str)

   def append_at_end(self, data):
      current_node = self.head
      while current_node.next:
         current_node = current_node.next

      current_node.next = Node(data, None)


if __name__ == '__main__':
   ll = LinkedList()

# item added at end
   ll.append_at_end(22)
   ll.append_at_end(44)
   ll.append_at_end(77)
   ll.append_at_end(55)
   ll.append_at_end(99)
   ll.append_at_end(11)
   
   ll.print_linked_list()