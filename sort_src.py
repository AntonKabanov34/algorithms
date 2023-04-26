src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def sort_src(x):
    """Функция сортировки списка. Принимает list возвращает list, сохраняет только те элементы, значения которых больше предыдущего"""
    flag = 0
    a = 0
    b = 1
    while flag < len(x) - 1:
        if x[a] >= x[b]:
            a += 1
            b += 1
        else:
            result.append(x[b])
            a += 1
            b += 1

        flag += 1






sort_src(src)
print(sort_src(),__doc__)
print(result)



src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []


def src_set(x):
    """Принимает list и возвращает отсортированный list с сохранением последовательности оригинального списка"""
    for i in x:
        a = 0  # метка старта
        flag = len(x) - 1
        score = 0

        while flag > 0:
            flag -= 1
            if i != x[a]:
                a += 1
            else:
                a += 1
                score += 1

        if score > 1:
            continue
        else:
            result.append(i)



print(src_set(src))
