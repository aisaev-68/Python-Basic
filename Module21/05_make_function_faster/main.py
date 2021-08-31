def calculating_math_func(data, val={1: 1}):
    if data not in val:
        i = max(val)
        for j in range(i + 1, data + 1):
            val[j] = val[j - 1] * j
    val[data] /= data ** 3
    result = val[data] ** 10
    return result


numb = int(input('Введите число: '))
print(calculating_math_func(numb))
