# 1 задание
my_age = 10
print(my_age)

# 2 задание
greeting = 'Father!'
print(greeting)

# 3 задание
time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

# 4 задание
n = 3
nn = 33
nnn = 333
a = n + nn + nnn
print(n + nn + nnn)

# 5 задание
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

# 6 задание
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 2
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 6
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
