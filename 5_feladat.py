my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

def add_elements_sum(my_list):
  for i in range(0,len(my_list)):
    my_list[i].append(my_list[i][0] + my_list[i][1])
  print(my_list)

add_elements_sum(my_list)