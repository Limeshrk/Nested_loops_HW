matrix = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

total = 0
for i in range(0,len(matrix)):
  for j in range(0,len(matrix[i])):
    total += matrix[i][j]
print(total)