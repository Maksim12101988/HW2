# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)



def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if arr[i] >= min_value and arr[i] <= max_value:
            indexes.append(i)
    return indexes

# Пример
lst = [2, 5, 1, 9, 3, 6, 7, 4]
min_val = 3
max_val = 6
result = find_indexes(lst, min_val, max_val)
print(f"Индексы элементов в диапазоне от {min_val} до {max_val}: ", result)






