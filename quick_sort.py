def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Before:", sample)
    print("After: ", quick_sort(sample))
