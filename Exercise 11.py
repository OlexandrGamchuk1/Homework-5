my_list = [7, 2, 9, 4]
for i in range(len(my_list)):
    x = my_list.pop(i)
    my_list.insert(0, x)
print(my_list)