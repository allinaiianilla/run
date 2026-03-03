def bubble_sort(arr):
    """In‑place bubble sort of a list."""
    n = len(arr)
    for i in range(n):
        # 每一轮冒泡，把最大的元素“冒”到末尾
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 示例
if __name__ == "__main__":
    data = [5, 3, 1, 4, 2]
    print("排序前：", data)
    bubble_sort(data)
    print("排序后：", data)