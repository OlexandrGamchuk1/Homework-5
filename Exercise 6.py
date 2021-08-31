my_list = []

for i in range(4):
    a = int(input('Enter the number '))
    my_list.append(a)

my_list1 = []

for i in my_list:
    my_list1.append(i * 2)
print(my_list + my_list1)