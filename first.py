#First excercise
#calculates the sum of the elements in a matrix
m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

def matrix_sum(matrix):
  summa = 0
  for row in matrix:
      for num in row:
          summa += num
  return summa

print(matrix_sum(m))