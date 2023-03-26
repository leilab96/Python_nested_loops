#Fourth Excercise

persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

def two_cycles(first_list,second_list):
  for i in first_list:
    for j in second_list:
      print(f"{i} eats {j}")
      
two_cycles(persons,restaurants)