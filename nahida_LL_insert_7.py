# Linked list insert implementation at spacific index

class Node:
   def  __init__(self, data = "Head" , next = None):
      self.data = data
      self.next = next

class LINKED_LIST:
   def __init__(self):
      self.head = Node()

   def get_length(self):
      cnt = 0
      current_node = self.head
      while current_node:
         cnt += 1
         current_node = current_node.next
      return cnt
   

   def insert(self,index, data):
      if index < 0 or index > self.get_length():
         print("Invalid Index")
         return

      if self.head.next == None:
         node = Node(data, self.head.next)
         self.head.next = node
         return

      if self.head.next == None:
         node = Node(data, self.head.next)
         self.head.next = node
         return

      cnt = 0
      current_node = self.head
      while current_node != None:
         if cnt == index -1:
               node = Node(data, current_node.next)
               current_node.next = node
               break
         current_node = current_node.next
         cnt += 1

   def display(self):
      if self.head.next is None:
         return "Empty"

      current_node = self.head
      info_str = ""
      while current_node:
         info_str = info_str + str (current_node.data) + ' --> '
         current_node = current_node.next

      return info_str 

if __name__ == '__main__' :
   LL = LINKED_LIST()

   LL.insert(1, 0)
   LL.insert(2, 2)
   LL.insert(3, 3)
   LL.insert(4, 4)
   print("Linked List: ", LL.display())
   LL.insert(2, 1)
   print("After inserton: ", LL.display())