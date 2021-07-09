#Selection Short Implementation

def selection_sort(data_list):
   length = len(data_list)

   for i in range(length - 1):
      min_index = i
      for j in range(i+1, length):
         if data_list[j] < data_list[min_index]:
            min_index = j
   
      if min_index != i:
         temp = data_list[i]
         data_list[i] = data_list[min_index]
         data_list[min_index] = temp

if __name__	 == '__main__':
   data_list = [10, 60, 1, 55, 5, 3, 80]
   selection_sort(data_list)
   print("sorted list: ", data_list)