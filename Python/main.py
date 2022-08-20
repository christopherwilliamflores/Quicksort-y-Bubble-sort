import time
import matplotlib.pyplot as plt
from random import randint as rd
from math import pow
import json

# Codigo de ordenamiento extraido de "https://stackabuse.com/quicksort-in-python/"


def partition(array, low, high):
    i = (low - 1)
    x = array[high]

    for j in range(low, high):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# low  --> Starting index,
# high  --> Ending index
def quick_sort(array, low, high):
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * size

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # sorted array
        p = partition(array, low, high)

        # push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

# Codigo de ordenamiento extraido de "https://www.techiedelight.com/es/bubble-sort-iterative-recursive/"


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def guardar_datos(data, file_name):
    file = open(file_name, "w")
    json.dump(data, file, indent=5)


def graficar(sz1, t1, sz2, t2):
    plt.figure(figsize=(8, 6))

    plt.scatter(sz1, t1)
    plt.plot(sz1, t1, color="blue", label="Quick Sort")
    plt.scatter(sz2, t2)
    plt.plot(sz2, t2, color="red", label="Bubble Sort")

    plt.grid()

    plt.yscale("log")
    plt.xscale("log")

    plt.xlabel("data size", fontsize=20)
    plt.ylabel("time (ms)", fontsize=20)
    plt.title("Plot with both log axes", fontsize=25)

    plt.legend()
    plt.show()


datos = {
    "quickSort": {
        "dataSize": [],
        "time": []
    },
    "bubbleSort": {
        "dataSize": [],
        "time": []
    }
}

numero_de_pruebas = 5
min_num = 0
max_num = 100_000
s_to_ms = 1_000

for i in range(numero_de_pruebas):
    numero_de_datos = int(pow(10, i + 1))
    print(f"Cantidad de datos: {numero_de_datos}")

    lista_aleatoria_quick_sort = [rd(min_num, max_num) for _ in range(numero_de_datos)]
    lista_aleatoria_bubble_sort = lista_aleatoria_quick_sort.copy()

    start_time = time.time()
    quick_sort(lista_aleatoria_quick_sort, 0, len(lista_aleatoria_quick_sort) - 1)
    end_time = time.time()
    tiempo_ordenamiento_ms = (end_time - start_time) * s_to_ms

    datos["quickSort"]["dataSize"].append(numero_de_datos)
    datos["quickSort"]["time"].append(tiempo_ordenamiento_ms)

    start_time2 = time.time()
    bubble_sort(lista_aleatoria_bubble_sort)
    end_time2 = time.time()
    tiempo_ordenamiento_ms = (end_time2 - start_time2) * s_to_ms

    datos["bubbleSort"]["dataSize"].append(numero_de_datos)
    datos["bubbleSort"]["time"].append(tiempo_ordenamiento_ms)

graficar(datos["quickSort"]["dataSize"], datos["quickSort"]["time"], datos["bubbleSort"]["dataSize"], datos["bubbleSort"]["time"])
guardar_datos(datos, "datos.json")
