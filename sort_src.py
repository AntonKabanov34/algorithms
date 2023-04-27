src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def sort_src(x):
    """Функция сортировки списка. Принимает list возвращает list, сохраняет только те элементы, значения которых
    больше предыдущего """
    index = 0
    while index < len(x) - 1:
        if x[index] <= x[index - 1]:
            result.append(x[index + 1])
            index += 1
        else:
            result.append(x[index])

        index += 1


sort_src(src)
print(sort_src.__doc__)
print(f'Исходник: {src}')
print(f'Сортировка: {result}\n')

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []


def src_set(x):
    """Функция сортировки списка. Принимает list и возвращает отсортированный list с сохранением последовательности
    оригинального списка """
    for i in x:
        index = 0  # метка старта
        flag = len(x) - 1
        score = 0

        while flag > 0:
            flag -= 1
            if i != x[index]:
                index += 1
            else:
                index += 1
                score += 1

        if score > 1:
            continue
        else:
            result.append(i)


src_set(src)
print(src_set.__doc__)
print(f'Исходник: {src}')
print(f'Сортировка: {result}')
