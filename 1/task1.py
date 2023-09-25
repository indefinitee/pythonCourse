list = [2, 4, 6, 7, 9, 8, 237, 2, 4]

for item in list:
    if item % 2 == 0:
        print(item)
    if item == 237:
        print("Ужас, Число 237!!!!")
        break
 