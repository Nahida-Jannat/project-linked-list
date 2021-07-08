#LinkedList implementation
#Function : insert_at()

class Node:
   def __init__(self, data= None, next= None):
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
#search data in a LinkeLlist
   def search(self, search_item):
      current_node = self.head.next

      while current_node != None:
         if current_node.data == search_item:
            print("Data found")
            return
         current_node = current_node.next

      print("Not found!")


# Add values at begining in linked list

   def append_at_begining(self,data):
      node = Node(data, self.head.next)
      self.head.next = node

if __name__ == '__main__':
   LL = LinkedList()
   LL.append_at_begining(10)
   LL.append_at_begining(20)
   LL.append_at_begining(30)
   LL.append_at_begining(40)
   LL.search(20)
   LL.print_linked_list()
