a = [0, 5, 2, 4, 7, 1, 3, 19]
b = len(a)
j = 0
for i in range(0, b):
    if a[i] % 2 == 0:
        continue
    j += 1
print(j)