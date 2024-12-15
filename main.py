import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Functii pentru sortare

def merge_sort(lst):
    # Sortează o listă folosind algoritmul Merge Sort, care are complexitatea O(n log n).
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

def heapify(lst, n, i):
    # Transformă o sublistă într-un heap maximizat pornind de la nodul `i`.
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:
        largest = left

    if right < n and lst[largest] < lst[right]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

def heap_sort(lst):
    # Sortează o listă folosind algoritmul Heap Sort, care are complexitatea O(n log n).
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

def radix_sort(lst):
    # Sortează o listă de numere întregi folosind algoritmul Radix Sort.
    max_val = max(lst)
    exp = 1
    while max_val // exp > 0:
        counting_sort(lst, exp)
        exp *= 10

def counting_sort(lst, exp):
    # Funcție auxiliară pentru Radix Sort, care sortează elementele după un anumit exponent.
    n = len(lst)
    output = [0] * n
    count = [0] * 10

    for i in lst:
        index = i // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = lst[i] // exp
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1

    for i in range(n):
        lst[i] = output[i]

def quick_sort(lst):
    # Sortează o listă folosind algoritmul Quick Sort, care are complexitatea medie O(n log n).
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Functia principala

def main():
    # Setări inițiale pentru generarea listelor de test și algoritmii de sortare.
    # Setările din cerință iau un timp imens de rulare, dar generează un rezultat mai precis.
    num_lists = 500
    min_len = 1000
    max_len = 10000

    sort_algorithms = {
        "Timsort (Python sorted)": sorted,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Radix Sort": radix_sort,
    }

    times = {name: [] for name in sort_algorithms}
    list_lengths = []

    for _ in range(num_lists):
        length = random.randint(min_len, max_len)
        lst = [random.randint(0, 1_000_000) for _ in range(length)]
        list_lengths.append(length)

        for name, sort_func in sort_algorithms.items():
            lst_copy = lst.copy()
            start_time = time.time()
            sort_func(lst_copy)
            end_time = time.time()
            times[name].append(end_time - start_time)

    # Analiza rezultatelor
    avg_times = {name: np.mean(times[name]) for name in sort_algorithms}

    print("\nRezultatele medii ale timpului de sortare:")
    for name, avg_time in avg_times.items():
        print(f"{name}: {avg_time:.4f} secunde")

    # Grafic
    plt.figure(figsize=(10, 6))
    for name, time_list in times.items():
        plt.plot(list_lengths, time_list, '.', label=name, alpha=0.5)

    plt.xlabel("Lungimea listei")
    plt.ylabel("Timpul de sortare (secunde)")
    plt.title("Performanța algoritmilor de sortare")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
