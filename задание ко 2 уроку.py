# 1 задание
print(list("cat"))
li = [1, 3, 5, 7, "My", 33.33, False]
print(li)
print(type)

# 2 задание
print(list("cat"))
li = [1, 3, 5, 7, "My", 33.33, False]
li[0], li[1] = li[1], li[0]
li[2], li[3] = li[3], li[2]
li[4], li[5] = li[5], li[4]
print(li)
st = input("My").lower()
print(st)
for word in st:
    if word(0) == "б": my
print(word)

# 3 задание
seasons_list = ["winter", 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[0])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[0])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[0])
else:
    print("Такого месяца не существует")

# 4 задание
st = "Как вас зовут"
res = st.split()
print(res)
st = "Как \nвас \nзовут"
li = ['как', 'вас', 'зовут']
for i, el in enumerate(li, 1):
    print(f"{1}, {el}")

# 5 задание "Рейтинг"
my_list = [1, 3, 10, 15, 21]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
print(f"текущий список - {my_list}")
digit = int(input("Введите число "))
