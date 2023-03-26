#Fifth Excercise
#Function will add another element to each element (in a list containing lists) and that element will be the some of the other elements in the list

my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

def element_sum (lists):
  for element in lists:
    element.append(sum(element))
  return lists  

print(element_sum(my_list))