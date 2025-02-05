import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    return sorted_list
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Wylosowane liczby:", random_numbers)
sorted_numbers = merge_sort(random_numbers)
print("Posortowane liczby:", sorted_numbers)
