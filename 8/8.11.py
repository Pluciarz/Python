import random

def sortowanie_przez_wybor(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
liczby_losowe = [random.randint(1, 100) for _ in range(10)]
print("Oryginalny ciąg liczb:", liczby_losowe)
sortowanie_przez_wybor(liczby_losowe)
print("Posortowany ciąg liczb:", liczby_losowe)
