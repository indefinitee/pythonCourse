a = int(input("Введите число: "))
b = int(input("Введите пограничное число: "))

if (a < b):
    print(f'Число {a} меньше {b}')
elif(a > b * 3):
    print(f'Число {a} больше числа {b}  аж более, чем в 3 раза!')
elif (a > b):
    print(f'Число {a} больше {b}')
