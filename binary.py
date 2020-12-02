def binarySearchRecursive(sequence, x, left, right):
    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] < x:
            left = mid + 1

        if sequence[mid] > x:
            right = mid - 1

        if sequence[mid] == x:
            return mid


if __name__ =="__main__":
    sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
    x = 77
    print('Index of number:', x, 'is equal to', binarySearchRecursive(sample, x, 0, len(sample)-1))