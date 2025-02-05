import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Wygenerowane liczby:", random_numbers)
sorted_numbers = quicksort(random_numbers)
print("Posortowane liczby:", sorted_numbers)
