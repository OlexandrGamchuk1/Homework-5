i = 1
my_list = []
while i <= 12:
    a = int(input(f'Enter salary for {i} month from 7500 to 15000: '))
    my_list.append(a)
    i += 1
print(my_list)
print(f'Average monthly salaryint {(int(sum(my_list) / 12))}')