import random

def sortowanie_przez_wstawianie(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
liczby_losowe = [random.randint(1, 100) for _ in range(10)]
print("Losowe liczby:", liczby_losowe)
sortowanie_przez_wstawianie(liczby_losowe)
print("Posortowane liczby:", liczby_losowe)