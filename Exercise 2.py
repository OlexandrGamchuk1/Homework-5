a = int(input('Enter the number '))
b = 1
if 4 < a < 16:
    for i in range(1, a + 1):
        b *= i
    print(b)