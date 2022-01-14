def selection_sort(arr):

    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                smallest = j
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr

print(selection_sort([2,34,2,4,2,4,2])) 