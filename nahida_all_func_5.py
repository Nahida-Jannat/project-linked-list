# linked list implementation
# add value at beginning, add value at end, insert value at specific index

class NODE:
   def __init__(self, data = "Head", next = None):
      self.data = data
      self.next = next

class LINKED_LIST:
   def __init__(self):
      self.head = NODE()

   def append_at_beginning(self, data):
      node = NODE(data, self.head.next)
      self.head.next = node

   def append_at_end(self, data):
      current_node = self.head
      while current_node.next:
         current_node = current_node.next
      current_node.next = NODE(data, None)

   def Get_length(self):
      cnt = 0
      current_node = self.head
      while current_node:
         cnt += 1
         current_node = current_node.next
      return cnt

   def insert_at(self, index, data):
      if index < 0 or index > self.Get_length():
         print("Invalid Index")
         return

      if index == 0:
         self.append_at_beginning(data)
         return

      cnt = 0
      current_node = self.head
      while current_node:
         if cnt == index - 1:
               node = NODE(data, current_node.next)
               current_node.next = node
               break
         current_node = current_node.next
         cnt += 1

   def printing(self):
      if self.head is None:
         print("Linked list is Empty")
         return

      current_node = self.head
      String = ""
      while current_node:
         String = String + str (current_node.data) + ' --> '
         current_node = current_node.next
      
      print(String)

LL = LINKED_LIST()

# append at beginning 
LL.append_at_beginning(616)
LL.append_at_beginning(520)
LL.append_at_beginning(770)
LL.printing()

# append at end
LL.append_at_end(852)
LL.append_at_end(954)
LL.append_at_end(333)
LL.printing()

# insert at specific index
LL.insert_at(3, 321)
LL.insert_at(5, 130)
LL.insert_at(6, 420)
LL.printing()