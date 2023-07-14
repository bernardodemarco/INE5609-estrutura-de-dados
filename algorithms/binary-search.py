def binary_search(arr: list[int], target: int) -> int | None:
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        if target == arr[middle]:
            return middle

        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1

    return None


# output -> 1
print(binary_search([1, 5, 9, 20, 27, 32, 40, 62, 70, 76, 77], 5))
# output -> None
print(binary_search([1, 5, 9, 20, 27, 32, 40, 62, 70, 76, 77], 4))
