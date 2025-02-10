start = int(input("Введите первое число: "))
end = int(input("Введите второе число: "))

if start > end:
    start, end = end, start

print("Нечетные числа в указанном диапазоне:")
i = start
while i <= end:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

print("\n")

count = 0
num = 100
while num <= 9999:
    str_num = str(num)
    unique = True
    for digit in str_num:
        if str_num.count(digit) > 1:
            unique = False
            break
    if unique:
        count += 1
    num += 1

print(f"Количество чисел с разными цифрами в диапазоне 100-9999: {count}")
