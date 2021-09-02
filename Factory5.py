import random
input_list = [1, 3, 4, 3, 3, 9]
#Генерируем случайное число не привышающие количество елементов массива
k = random.randint(0, len(input_list))
list_result = []


while k > 0:
    # Генерируем индекс не выходящий за длинну массива
    b = random.randint(0, len(input_list) - 1)
    # Добавляем число в итоговый список
    list_result.append(input_list[b])
    # Удаляем элемент из начального списка что бы избежать повторений
    input_list.pop(b)
    k -= 1
print(list_result)


input_list = [1, 3, 4, 3, 3, 9]
#Генерируем случайное число не привышающие количество елементов массива
k = random.randint(0, len(input_list))
list_result = []
index_list = []
print(k)
while k > 0:
    # Генерируем индекс не выходящий за длинну массива
    b = random.randint(0, len(input_list) - 1)
    # Проверка на повторение
    if b in index_list:
        # Если проверка не пройдена минуем оставшееся тело цикла
        continue
    # Если проверка пройдена добавляем число в итоговый список и индекс в
    # список индексов для проверки на повторение
    else:
        list_result.append(input_list[b])
        index_list.append(b)
        k -= 1



print(list_result)