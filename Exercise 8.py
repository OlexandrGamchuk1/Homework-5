my_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
a = 0
for i in my_matrix:
    print(i)
    for j in i:
        a += j
print(f'Sum {a}')