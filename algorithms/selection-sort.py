def selection_sort(arr: list[int]) -> list[int]:
    for min_search_idx in range(len(arr) - 1):
        min_idx = min_search_idx
        for i in range(min_search_idx + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[min_search_idx], arr[min_idx] = arr[min_idx], arr[min_search_idx]
    return arr


sorted_arr = selection_sort(
    [15, 2, 6, 9, 72, 56, 27, 31, 78, 24, 67, 32, 61, 25])
print(sorted_arr)
