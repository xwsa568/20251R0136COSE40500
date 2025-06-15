def bubble_sort(arr):
    """
    Bubble Sort 알고리즘
    :param arr: 정렬할 리스트
    :return: 오름차순으로 정렬된 리스트
    """
    n = len(arr)
    for i in range(n):
        # 마지막 i개는 이미 정렬되어 있으므로 제외
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Before:", sample)
    print("After: ", bubble_sort(sample))
