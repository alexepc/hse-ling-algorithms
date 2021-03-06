def key(x):
    # Функция вычисления ключа сравнения для `sorted`.
    # Перепишите её так, чтобы она реализовала
    # натуральную сортировку строк состоящих из символов a-z0-9.

    # Функция не должна использовать регулярные выражения!

    # Для "обычной" посимвольной сортировки она могла
    # бы выглядеть так:
    # return tuple(c for c in x)
    res = []
    ind = 0
    str_num = ''
    while ind < len(x):
        if x[ind] in '0123456789':
            str_num += x[ind]
            ind += 1
        else:
            if str_num != '':
                res.append(int(str_num)+1000)
                str_num = ''
            res.append(ord(x[ind]))
            ind += 1
    if str_num != '':
        res.append(int(str_num)+1000)
    return res

# # print(sorted(['lol3llll23', 'a10', 'lol2ggdf45', 'lol100k5k', 'lol11', 'lol21', 'a1', 'lol2ggdf46'], key=key))
# print(sorted(['a1', 'a10', 'b', '0', '200', '-1000', '1000000'], key=key))
# print(sorted(['img9b12', 'img10a11', 'img10a', 'img10a10'], key=key))
# print(sorted(['a1', 'a10', 'b', '0', '200'], key=key))
# print(sorted(['a1', 'a10', 'b', '0', '1200'], key=key))
# print(sorted(['img10a10', 'img10a11', 'img10a'], key=key))
