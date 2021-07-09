#Selection short implementation in Python

def selection_short(data_list):
   length = len(data_list)

   for i in range(length - 1):
      min_index =i
      for j in range(i + 1, length):
         if data_list[j] < data_list[min_index]:
            min_index = j

      if min_index != i:
         temp = data_list[i]
         data_list[i] = data_list[min_index]
         data_list[min_index] = temp

if __name__ == "__main__":
   #
   data_list = [55, 10, 80, 66, 5, 70, 2]
   selection_short(data_list)
   print('Shorted List: ', data_list)


