
# # Sum the numbers
numbers = [21, 30, 40, 50]
print(sum(numbers))

# # Largest Number
num = [1, 10, 20, 30, 40]
print(max(num))

# # Smallest number
num = [1, 10, 20, 30, 40]
print(min(num))

# # Even numbers
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
    if i % 2 == 0:
        print(i)

# # Positive Numbers
num = [-10, 3, 4, -6, -1, 5]
for i in num:
    if i > 0:
        print(i)

# Positive Numbers II
num = [-10, 3, 4, -6, -1, 5]
pos = []
for i in num:
    if i > 0: 
        pos.append(i)
print(pos)

# Multiply a list
num = [1, 2, 3, 4, 5]
results = []
for i in num:
    results.append(i * 5)
print(results)

# Multiply vectors
list1 = [1, 2, 3]
list2 = [2, 4, 6]
results = []

for i in range(0, len(list1)):
    results.append(list1[i]*list2[i])
print(results)

# Matrix Addition
mat_1 = [ [1, 2],
          [5, 7] ]
mat_2 = [ [3, 4],
          [9, 8] ]
result = [[0,0], 
          [0,0]] 

for i in range(len(mat_1)):
    for j in range(len(mat_1[0])):
        result[i][j] = mat_1[i][j] + mat_2[i][j]
print(result)

# Matrix Addition II
mat_1 = [ [1, 2, 9],
          [5, 7, 2] ]
mat_2 = [ [3, 4, 1],
          [9, 8, 7] ]
result = [[0,0, 0], 
          [0,0, 0]] 

for i in range(len(mat_1)):
    for j in range(len(mat_1[0])):
        result[i][j] = mat_1[i][j] + mat_2[i][j]
print(result)

# De-dup
list1 = [1, 1, 2, 2, 3, 4, 5, 5]
list1 = list(dict.fromkeys(list1))
print(list1)

# Matrix Multiplication
mat_1 = [ [1, 2],
          [5, 7] ]
mat_2 = [ [3, 4],
          [9, 8] ]
result = [[0, 0], 
          [0, 0]] 

for i in range(len(mat_1)):
    for j in range(len(mat_1[0])):
        result[i][j] = mat_1[i][j] * mat_2[i][j]
print(result)

        

